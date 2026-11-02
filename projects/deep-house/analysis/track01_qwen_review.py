"""Local, anonymous audio-caption cross-checks for first-track clips only."""
import argparse,json,time,os
from pathlib import Path
import numpy as np
import soundfile as sf
import torch
from transformers import AutoProcessor,Qwen2AudioForConditionalGeneration,BitsAndBytesConfig

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--model-dir',required=True);ap.add_argument('--manifest',required=True);ap.add_argument('--output',required=True);args=ap.parse_args()
    torch.set_num_threads(4)
    clips=json.loads(Path(args.manifest).read_text(encoding='utf-8'))
    assert all(0<=c['start_s']<c['end_s']<=222 for c in clips)
    out=Path(args.output);out.mkdir(parents=True,exist_ok=True)
    prompt=('Describe the audible foreground and background sound layers and their musical roles in this clip. '
            'Describe the tone, attack and sustain of the repeating pitched sounds. '
            'Report any identifiable human voice, sung or spoken words, or uncertainty about voice-like sounds. '
            'Do not assume there is a voice. Do not invent exact chords, artists, equipment or effect settings. '
            'Answer only about this audio, in under 150 words.')
    quant=BitsAndBytesConfig(load_in_4bit=True,bnb_4bit_quant_type='nf4',bnb_4bit_compute_dtype=torch.float16,bnb_4bit_use_double_quant=True,llm_int8_skip_modules=['audio_tower','multi_modal_projector'])
    print('LOADING_PROCESSOR',flush=True)
    processor=AutoProcessor.from_pretrained(args.model_dir,local_files_only=True)
    print('LOADING_QWEN_4BIT',flush=True);start=time.time()
    model=Qwen2AudioForConditionalGeneration.from_pretrained(args.model_dir,local_files_only=True,quantization_config=quant,torch_dtype=torch.float16,device_map={'':0},attn_implementation='sdpa').eval()
    print('MODEL_READY',round(time.time()-start,1),'allocated_GB',round(torch.cuda.memory_allocated()/1024**3,2),flush=True)
    meta={'model':'Qwen/Qwen2-Audio-7B-Instruct','revision':'0a095220c30b7b31434169c3086508ef3ea5bf0a','quantization':'NF4 double quantization; audio_tower and multi_modal_projector excluded','compute_dtype':'float16','device':'cuda:0','prompt':prompt,'max_new_tokens':200,'do_sample':False,'load_seconds':time.time()-start}
    (out/'qwen_run_config.json').write_text(json.dumps(meta,indent=2),encoding='utf-8')
    for clip in clips:
        target=out/(clip['id']+'_qwen.json')
        if target.exists():continue
        t=time.time();record={**clip,'prompt':prompt}
        try:
            y,sr=sf.read(clip['input_path'],dtype='float32');assert sr==16000 and y.ndim==1
            conv=[{'role':'user','content':[{'type':'audio','audio_url':'clip.wav'},{'type':'text','text':prompt}]}]
            text=processor.apply_chat_template(conv,add_generation_prompt=True,tokenize=False)
            inputs=processor(text=text,audio=[y],sampling_rate=sr,return_tensors='pt',padding=True)
            if 'input_features' not in inputs:
                raise RuntimeError('Audio features were not created; refusing text-only inference.')
            record['input_tensor_shapes']={k:list(v.shape) for k,v in inputs.items()}
            record['audio_feature_absolute_sum']=float(inputs['input_features'].abs().sum())
            inputs={k:v.to('cuda') for k,v in inputs.items()}
            if 'input_features' in inputs:inputs['input_features']=inputs['input_features'].to(torch.float16)
            torch.cuda.reset_peak_memory_stats()
            with torch.inference_mode():ids=model.generate(**inputs,max_new_tokens=200,do_sample=False)
            answer=processor.batch_decode(ids[:,inputs['input_ids'].shape[1]:],skip_special_tokens=True,clean_up_tokenization_spaces=False)[0]
            record.update(response=answer,peak_cuda_gb=torch.cuda.max_memory_allocated()/1024**3)
            print('QWEN_RESPONSE',clip['id'],answer,flush=True)
        except Exception as e:
            record['error']=repr(e);print('QWEN_ERROR',clip['id'],repr(e),flush=True)
            if isinstance(e,torch.cuda.OutOfMemoryError):
                target.write_text(json.dumps(record,indent=2,ensure_ascii=False),encoding='utf-8');raise
        record['elapsed_s']=time.time()-t;target.write_text(json.dumps(record,indent=2,ensure_ascii=False),encoding='utf-8')
    print('QWEN_REVIEW_FINISHED',flush=True)
if __name__=='__main__':main()
