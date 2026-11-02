"""Analyze only the first 222 seconds. Output audio/features stay under ignored local/."""
from pathlib import Path
import json, csv, time
import numpy as np
import soundfile as sf
import scipy.signal as ss
from scipy.ndimage import gaussian_filter1d
from scipy.optimize import minimize
import librosa
import pyloudnorm as pyln
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'local/deep-house/first_track_20261102'
SR = 22050
END = 222
PARTS = ['bass','drums','guitar','other','piano','vocals']

def db(x):
    return 20*np.log10(np.maximum(np.asarray(x),1e-12))

def band(x, lo, hi, sr=SR):
    sos=ss.butter(4,[lo,hi],btype='bandpass',fs=sr,output='sos')
    return ss.sosfiltfilt(sos,x,axis=0).astype(np.float32)

def mono_load(p):
    x,sr=sf.read(p,frames=44100*END,dtype='float32',always_2d=True)
    return librosa.resample(x.mean(axis=1),orig_sr=sr,target_sr=SR)

def summaries(x,sr,step=4):
    return [float(db(np.sqrt(np.mean(x[int(t*sr):int(min(t+step,END)*sr)]**2)))) for t in range(0,END,step)]

def envelope(x, sr=SR, rate=200):
    h=max(1,int(sr/rate)); z=ss.resample_poly(x*x,rate,sr)
    return np.sqrt(np.maximum(gaussian_filter1d(z,1.2),0))

def stereo_stats(x):
    l,r=x[:,0],x[:,1];m=(l+r)/2;s=(l-r)/2
    return {'lr_correlation':float(np.corrcoef(l,r)[0,1]),'side_mid_db':float(db(np.sqrt(np.mean(s*s))/max(np.sqrt(np.mean(m*m)),1e-12)))}

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    stereo,sr=sf.read(OUT/'track01_original_0_222.wav',dtype='float32',always_2d=True)
    assert sr==44100 and len(stereo)==sr*END
    mono=librosa.resample(stereo.mean(axis=1),orig_sr=sr,target_sr=SR)
    result={'sr':sr,'seconds':len(stereo)/sr,'peak_dbfs':float(db(np.max(np.abs(stereo)))),'rms_dbfs':float(db(np.sqrt(np.mean(stereo**2)))),'lufs':float(pyln.Meter(sr).integrated_loudness(stereo)),'stereo':stereo_stats(stereo),'versions':{'librosa':librosa.__version__}}
    print('MASTER',json.dumps(result),flush=True)
    series={'master':summaries(mono,SR)}; stems={};stemstats={}
    for model in ['demucs','sw']:
        total=np.zeros_like(mono);stemstats[model]={};stems[model]={}
        for part in PARTS:
            if model=='demucs':p=ROOT/f'local/deep-house/reference/stems/htdemucs_6s/R01_Lost in the Echoes/{part}.wav'
            else:p=ROOT/f'local/deep-house/reference/stems_sw/R01_Lost in the Echoes/R01_Lost in the Echoes_({part})_BS-Roformer-SW.wav'
            y=mono_load(p)[:len(mono)]; stems[model][part]=y;total+=y
            series[f'{model}_{part}']=summaries(y,SR)
            stemstats[model][part]={'rms_dbfs':float(db(np.sqrt(np.mean(y*y)))),'rms_vs_master_db':float(db(np.sqrt(np.mean(y*y))/np.sqrt(np.mean(mono*mono))))}
        gain=float(np.dot(total,mono)/np.dot(total,total))
        stemstats[model]['sum_check']={'best_gain':gain,'correlation':float(np.corrcoef(total,mono)[0,1]),'residual_to_master_db':float(db(np.sqrt(np.mean((gain*total-mono)**2))/np.sqrt(np.mean(mono**2))))}
    result['stem_stats']=stemstats
    print('STEMS',json.dumps(stemstats),flush=True)
    # Frequency energies and stereo width in the original; no instrument labels inferred.
    bands=[(25,80),(80,200),(200,500),(500,2000),(2000,6000),(6000,16000)]
    result['frequency_bands']={}
    for lo,hi in bands:
        z=band(stereo,lo,hi,sr);e=float(np.mean(z*z))
        result['frequency_bands'][f'{lo}_{hi}']={'rms_dbfs':float(db(np.sqrt(e))),'power_fraction':e/float(np.mean(stereo**2)),**stereo_stats(z)}
    # Kick-like low pulses from two independently separated drum estimates.
    pulses={}
    for model in ['demucs','sw']:
        e=envelope(band(stems[model]['drums'],30,160))
        smooth=gaussian_filter1d(e,0.7)
        p,_=ss.find_peaks(smooth,distance=0.23*200,prominence=np.percentile(smooth,90)*0.18)
        t=p/200;w=smooth[p];pulses[model]=(t,w)
        np.savetxt(OUT/f'{model}_low_pulses.csv',np.c_[t,w],delimiter=',',header='time_s,strength',comments='')
        strong=t[(t>25)&(t<195)]
        dt=np.diff(strong);good=dt[(dt>.32)&(dt<.8)]
        hist,edges=np.histogram(good,bins=np.arange(.32,.805,.005));period=float((edges[np.argmax(hist)]+edges[np.argmax(hist)+1])/2)
        tempi=[]
        for start in [16,64,112,160]:
            clip=stems[model]['drums'][start*SR:(start+32)*SR]
            oe=librosa.onset.onset_strength(y=clip,sr=SR,hop_length=256)
            temp=librosa.feature.tempo(onset_envelope=oe,sr=SR,hop_length=256,start_bpm=110,max_tempo=190)
            tempi.append({'start_s':start,'bpm':float(temp[0])})
        # Circular timing fit; no presumption that a pulse marks beat 1 of a bar.
        def loss(v):
            per,phase=v;d=((strong-phase+per/2)%per)-per/2
            return float(np.mean(np.minimum(d*d,.07**2)))
        fits=[]
        for scale in [.5,1,2]:
            per=period*scale
            if not .28<per<1.6:continue
            for ph in np.linspace(0,per,24,endpoint=False):
                f=minimize(loss,[per,ph],method='Nelder-Mead',options={'maxiter':500,'xatol':1e-10})
                if .28<f.x[0]<1.6:fits.append((float(f.fun),float(f.x[0]),float(f.x[1]%f.x[0])))
        fits.sort();best=next((f for f in fits if abs(f[1]-period)<.05),fits[0]);_,per,phase=best
        residual=((strong-phase+per/2)%per)-per/2
        result.setdefault('rhythm',{})[model]={'pulse_count':len(t),'interval_mode_s':period,'bpm_fit':60/per,'period_s':per,'phase_s':phase,'pulse_abs_residual_median_ms':float(np.median(abs(residual))*1000),'pulse_abs_residual_p90_ms':float(np.percentile(abs(residual),90)*1000),'librosa_windows':tempi,'fit_candidates':fits[:8]}
    print('RHYTHM',json.dumps(result['rhythm']),flush=True)
    per=result['rhythm']['sw']['period_s'];phase=result['rhythm']['sw']['phase_s']
    # Fold band-specific drum energy on a four-beat grid. Downbeat origin is provisional.
    step=per/4; grid=np.arange(phase,END,step)
    patterns={}
    for label,lo,hi in [('low',30,160),('mid',180,2000),('high',3000,10000)]:
        env=envelope(band(stems['sw']['drums'],lo,hi))
        vals=np.array([np.max(env[max(0,int((t-.015)*200)):min(len(env),int((t+.045)*200))]) if int((t+.045)*200)>0 else 0 for t in grid])
        mask=(grid>=40)&(grid<180)
        pattern=[float(np.median(vals[mask&(np.arange(len(grid))%16==i)])) for i in range(16)]
        norm=max(pattern) or 1;patterns[label]=[round(v/norm,3) for v in pattern]
    result['provisional_16_step_pattern']=patterns
    # Full-track spectral distribution and one-second spectral/energy history.
    S=abs(librosa.stft(mono,n_fft=4096,hop_length=512))**2;freq=librosa.fft_frequencies(sr=SR,n_fft=4096)
    result['spectral_centroid_hz_median']=float(np.median(librosa.feature.spectral_centroid(S=np.sqrt(S),sr=SR)[0]))
    result['sections_4s']=[{'start_s':i*4,'end_s':min((i+1)*4,END),**{k:round(v[i],2) for k,v in series.items()}} for i in range(len(series['master']))]
    # Source separation agreement is a diagnostic, not accuracy.
    result['cross_model_stem_correlations']={p:(float(np.corrcoef(stems['sw'][p],stems['demucs'][p])[0,1]) if np.std(stems['sw'][p])>1e-10 and np.std(stems['demucs'][p])>1e-10 else None) for p in PARTS}
    (OUT/'signal_results.json').write_text(json.dumps(result,indent=2,allow_nan=False),encoding='utf-8')
    with (OUT/'section_energy_4s.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(result['sections_4s'][0]));w.writeheader();w.writerows(result['sections_4s'])
    # Diagnostic figures, not perceptual proof.
    fig,ax=plt.subplots(4,1,figsize=(15,13),sharex=True)
    t=np.arange(len(mono))/SR;ax[0].plot(t[::100],mono[::100],lw=.3);ax[0].set_ylabel('Waveform')
    times=np.arange(S.shape[1])*512/SR
    ax[1].pcolormesh(times,freq,10*np.log10(S+1e-12),vmin=-50,vmax=25,shading='auto',cmap='magma');ax[1].set_yscale('log');ax[1].set_ylim(30,10000);ax[1].set_ylabel('Frequency Hz')
    colors={'drums':'#d84a4a','bass':'#276ab3','other':'#12935c','piano':'#aa6d23','guitar':'#9d66bb','vocals':'#555'}
    ts=np.arange(len(series['master']))*4+2
    for part in PARTS:ax[2].plot(ts,series['sw_'+part],label=part,color=colors[part]);ax[2].set_ylabel('SW stem RMS dBFS')
    ax[2].legend(ncol=6);ax[2].set_ylim(-65,-10)
    for lo,hi in [(25,160),(160,2000),(2000,16000)]:
        z=band(stereo,lo,hi,sr);width=[stereo_stats(z[int(s*sr):int(min(s+4,END)*sr)])['side_mid_db'] for s in range(0,END,4)]
        ax[3].plot(ts,width,label=f'{lo}-{hi} Hz')
    ax[3].legend();ax[3].set_ylabel('Side/Mid dB');ax[3].set_xlabel('Seconds within first track');ax[3].set_xlim(0,END)
    fig.tight_layout();fig.savefig(OUT/'track01_overview.png',dpi=150);plt.close(fig)
    print('COMPLETE',OUT,flush=True)

if __name__=='__main__':main()
