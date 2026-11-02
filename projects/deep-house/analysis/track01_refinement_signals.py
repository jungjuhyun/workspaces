"""Original-referenced envelope and pitch-palette refinement. No other tracks read."""
from pathlib import Path
import json
import numpy as np
import scipy.signal as ss
from scipy.ndimage import gaussian_filter1d
import soundfile as sf
import librosa
ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'local/deep-house/first_track_20261102'
OUT=BASE/'refinement'
def load(part,model='sw',sr=22050):
    if part=='original':p=BASE/'track01_original_0_222.wav'
    elif model=='sw':p=ROOT/f'local/deep-house/reference/stems_sw/R01_Lost in the Echoes/R01_Lost in the Echoes_({part})_BS-Roformer-SW.wav'
    else:p=ROOT/f'local/deep-house/reference/stems/htdemucs_6s/R01_Lost in the Echoes/{part}.wav'
    x,s=sf.read(p,frames=44100*222,dtype='float32',always_2d=True)
    return librosa.resample(x.mean(axis=1),orig_sr=s,target_sr=sr)
def env(x,lo,hi,sr=22050):
    z=ss.sosfiltfilt(ss.butter(4,[lo,hi],btype='bandpass',fs=sr,output='sos'),x)
    return np.sqrt(np.maximum(gaussian_filter1d(ss.resample_poly(z*z,1000,sr),1),0))
def main():
    OUT.mkdir(exist_ok=True);base=json.loads((BASE/'signal_results.json').read_text());per=base['rhythm']['sw']['period_s'];phase=base['rhythm']['sw']['phase_s']
    result={'note':'Envelope crossings are operational signal measures, not sample-accurate attacks, physical note retriggers or subjective quality scores. Causal interpretation remains separate.'}
    rows=[]
    for model in ['sw','demucs']:
        drums=load('drums',model)
        for label,lo,hi,offset in [('low_kick',30,160,0),('mid_backbeat',180,2000,0),('high_offbeat',3000,10000,per*.43)]:
            e=env(drums,lo,hi)
            for section,a,b in [('body_A',40,72),('body_B',112,144),('return',168,200)]:
                records=[]
                for i,t in enumerate(np.arange(phase,222,per)):
                    if not a<t<b:continue
                    if label=='mid_backbeat' and i%2==0:continue
                    center=t+offset;ia=max(0,int((center-.1)*1000));ib=min(len(e),int((center+.1)*1000))
                    peak=ia+np.argmax(e[ia:ib]);height=e[peak]
                    if height<1e-8:continue
                    pre=max(ia,peak-150);post=min(len(e),peak+int(per*.65*1000))
                    before=e[pre:peak+1];after=e[peak:post];loidx=np.flatnonzero(before<=height*.1);hiidx=np.flatnonzero(before>=height*.9)
                    if not len(loidx) or not len(hiidx):continue
                    onset=pre+loidx[-1];rise90=pre+hiidx[0]
                    decay=np.flatnonzero(after<=height*.1)
                    records.append({'peak_s':peak/1000,'envelope_10pct_s':onset/1000,'rise_10_90_ms':max(0,rise90-onset),'decay_peak_to_10pct_ms':int(decay[0]) if len(decay) else None,'peak_amplitude':float(height),'peak_minus_grid_ms':(peak/1000-center)*1000})
                if records:
                    attack=[r['rise_10_90_ms'] for r in records];decay=[r['decay_peak_to_10pct_ms'] for r in records if r['decay_peak_to_10pct_ms'] is not None]
                    rows.append({'model':model,'layer':label,'section':section,'interval_s':[a,b],'event_count':len(records),'rise_10_90_ms_median':float(np.median(attack)),'rise_10_90_ms_iqr':np.percentile(attack,[25,75]).tolist(),'decay_to_10_ms_median':float(np.median(decay)) if decay else None,'decay_uncensored_count':len(decay),'events':records})
    result['event_envelopes']=rows
    # Compare note occupancy rather than interpreting each neural event as a new note.
    notes=json.loads((BASE/'sw_other_basic_pitch.json').read_text())['notes'];cells=[]
    for label,a,b in [('intro',0,18),('body_A',39,72),('body_B',112,144),('break',149,167),('return',168,203),('outro',214,222)]:
        weights={}
        for n in notes:
            overlap=max(0,min(b,n['end_s'])-max(a,n['start_s']))
            if overlap:weights[n['midi']]=weights.get(n['midi'],0)+overlap*n['amplitude']
        total=sum(weights.values()) or 1
        cells.append({'section':label,'start_s':a,'end_s':b,'top_notes':[{'midi':k,'note':librosa.midi_to_note(k),'relative_duration_amplitude_weight':v/total} for k,v in sorted(weights.items(),key=lambda x:-x[1])[:8]]})
    result['upper_note_palette_by_section']=cells
    # Describe the sparse intro layer with onset/energy candidates, without naming its source.
    other=load('other');intro=other[:18*22050];oe=librosa.onset.onset_strength(y=intro,sr=22050,hop_length=128)
    onsets=librosa.onset.onset_detect(onset_envelope=oe,sr=22050,hop_length=128,units='time',backtrack=False)
    result['intro_other_spectral_onsets_s']=onsets.tolist()
    # Candidate voice-like events with their actual levels in the mix.
    voice=load('vocals');original=load('original');events=[]
    venv=env(voice,180,1800);smooth=gaussian_filter1d(venv,20);idx,_=ss.find_peaks(smooth,distance=600,prominence=np.percentile(smooth,95)*.25)
    for i in idx:
        t=i/1000;a=max(0,t-.25);b=min(222,t+.25);v=voice[int(a*22050):int(b*22050)];o=original[int(a*22050):int(b*22050)]
        level=20*np.log10(max(np.sqrt(np.mean(v*v)),1e-12));relative=20*np.log10(max(np.sqrt(np.mean(v*v)),1e-12)/max(np.sqrt(np.mean(o*o)),1e-12))
        if level>-45:events.append({'time_s':round(t,3),'stem_rms_dbfs':float(level),'stem_vs_original_rms_db':float(relative)})
    result['voice_assigned_event_candidates']=events
    (OUT/'refinement_signal_results.json').write_text(json.dumps(result,indent=2,ensure_ascii=False,allow_nan=False,default=lambda v:v.item()),encoding='utf-8')
    print('ENVELOPE_SUMMARY',json.dumps([{k:v for k,v in x.items() if k!='events'} for x in rows]),flush=True)
    print('UPPER_PALETTE',json.dumps(cells,ensure_ascii=False),flush=True)
    print('VOICE_ASSIGNED_EVENTS',json.dumps(events),flush=True)
if __name__=='__main__':main()
