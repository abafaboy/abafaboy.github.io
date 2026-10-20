#!/usr/bin/env python3
"""Independently verify narration assembly, input provenance and MP3 decoding.

This is byte/sample analysis. It does not listen to audio or run recognition.
"""
import argparse
import collections
import hashlib
import json
import math
from pathlib import Path
import re
import subprocess
import wave

import numpy as np

PACKAGE = Path(__file__).resolve().parents[1]
OUT = PACKAGE / 'qa'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def read_json(path):
    return json.loads(path.read_text())


def read_wav(path):
    with wave.open(str(path), 'rb') as wav:
        metadata = {'channels':wav.getnchannels(),'sample_width_bytes':wav.getsampwidth(),
                    'sample_rate':wav.getframerate(),'frames':wav.getnframes(),'compression':wav.getcomptype()}
        pcm = wav.readframes(wav.getnframes())
    return metadata,pcm


def signal_metrics(original, decoded):
    count = min(len(original),len(decoded))//2
    sx=sy=sxx=syy=sxy=err2=0.0
    for at in range(0,count,24000):
        end=min(at+24000,count)
        x=np.frombuffer(original[at*2:end*2],dtype='<i2').astype(np.float64)
        y=np.frombuffer(decoded[at*2:end*2],dtype='<i2').astype(np.float64)
        sx+=float(x.sum());sy+=float(y.sum())
        sxx+=float(np.dot(x,x));syy+=float(np.dot(y,y));sxy+=float(np.dot(x,y))
        delta=x-y;err2+=float(np.dot(delta,delta))
    denom=math.sqrt(max(0,(sxx-sx*sx/count)*(syy-sy*sy/count))) if count else 0
    return {'sample_frames_compared':count,
            'correlation_same_sample_alignment':(sxy-sx*sy/count)/denom if denom else None,
            'signal_to_error_db':10*math.log10(sxx/err2) if err2 and sxx else None,
            'rms_pcm16':math.sqrt(sxx/count) if count else None,
            'decoded_rms_pcm16':math.sqrt(syy/count) if count else None}


def main():
    global PACKAGE, OUT
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--package', type=Path, default=PACKAGE)
    parser.add_argument('--build', type=Path, required=True)
    parser.add_argument('--output-directory', type=Path, default=OUT)
    args = parser.parse_args()
    PACKAGE = args.package.resolve(strict=True)
    OUT = args.output_directory.resolve()
    OUT.mkdir(parents=True, exist_ok=True)
    paths = {'assembled_wav':args.build/'ch/005/audio.wav',
             'encoded_mp3':args.build/'ch/005/audio.mp3',
             'recordings_json':PACKAGE/'recordings/recordings.json',
             'timing_json':args.build/'timing.private.json',
             'source_script':PACKAGE/'source/lettering_script.json',
             'synthesis_code':PACKAGE/'tools/synthesize_kokoro.py'}
    inputs={key:{'path':str(path),'bytes':path.stat().st_size,'sha256':digest(path.read_bytes())} for key,path in paths.items()}
    recordings=read_json(paths['recordings_json'])['recordings']
    timing=read_json(paths['timing_json'])
    source=read_json(paths['source_script'])
    errors=[]
    def require(condition,message):
        if not condition: errors.append(message)
    source_lines=[]
    for panel in source['panels']:
        for i,item in enumerate(panel['items'],1):
            if item['kind']!='dialogue':
                continue
            source_lines.append({'id':f'p{panel["panel"]:03d}_l{i:02d}','panel':panel['panel'],'line':i,**item})
    require(len(source_lines)==len(recordings)==len(timing['lines'])==56,'Expected exactly 56 source, recording and timing records')
    require([r['id'] for r in recordings]==[r['id'] for r in source_lines],'Recording order differs from approved source')
    require([r['id'] for r in timing['lines']]==[r['id'] for r in source_lines],'Timing order differs from approved source')
    require(len({r['id'] for r in recordings})==56,'Duplicate recording IDs')
    require(len({r['id'] for r in timing['lines']})==56,'Duplicate timing IDs')
    require(not timing.get('test_only'),'Timing marked test_only')
    rate=timing['sample_rate']
    metadata,assembled=read_wav(paths['assembled_wav'])
    require(metadata['channels']==1 and metadata['sample_width_bytes']==2 and metadata['sample_rate']==rate==24000 and metadata['compression']=='NONE','Assembled WAV format differs from PCM16 mono 24000Hz')
    require(metadata['frames']==timing['duration_samples'] and len(assembled)==metadata['frames']*2,'Assembled framecount differs from timing')
    by_record={r['id']:r for r in recordings};by_time={r['id']:r for r in timing['lines']}
    payloads={};line_results=[];name_evidence=[]
    for s in source_lines:
        id_=s['id'];record=by_record[id_];t=by_time[id_]
        for field in ['speaker','text']:
            require(record.get(field)==s[field],f'{id_}: recording {field} differs from approved source')
            require(t.get(field)==s[field],f'{id_}: timing {field} differs from approved source')
        require(t['panel']==s['panel'] and t['line']==s['line'],f'{id_}: timing source coordinates differ')
        cast=timing['cast'][s['speaker']]
        for field in ['engine','voice_id','settings']:
            require(record.get(field)==cast.get(field),f'{id_}: recording {field} differs from declared cast')
        path=PACKAGE/'recordings'/record['wav']
        meta,pcm=read_wav(path);payloads[id_]=pcm
        require(meta['channels']==1 and meta['sample_width_bytes']==2 and meta['sample_rate']==rate and meta['compression']=='NONE',f'{id_}: WAV format differs')
        n=len(pcm)//2
        require(n==meta['frames']==record['samples']==t['samples']==t['end_sample']-t['start_sample'],f'{id_}: sample counts differ')
        require(digest(path.read_bytes())==record['sha256']==t['sha256'],f'{id_}: WAV file hashes differ')
        require(abs(record['duration']-n/rate)<1e-10,f'{id_}: recording duration differs')
        require(abs(t['start']-t['start_sample']/rate)<1e-10 and abs(t['end']-t['end_sample']/rate)<1e-10,f'{id_}: seconds/sample timestamps differ')
        snippet=assembled[t['start_sample']*2:t['end_sample']*2]
        exact=snippet==pcm
        require(exact,f'{id_}: declared assembled sample interval does not contain the entire exact normalized WAV payload')
        positions=[];offset=assembled.find(pcm)
        while offset>=0:
            if offset%2==0:positions.append(offset//2)
            offset=assembled.find(pcm,offset+1)
        require(positions==[t['start_sample']],f'{id_}: exact frame-aligned payload occurrences differ from one declared occurrence: {positions}')
        values=np.frombuffer(pcm,dtype='<i2').astype(np.int32)
        peak=int(np.max(np.abs(values)))
        require(peak==t['peak_pcm16'],f'{id_}: measured peak differs from timeline')
        require(peak>0 and peak<32767,f'{id_}: silent or full-scale clipped normalized payload')
        line_results.append({'id':id_,'speaker':s['speaker'],'text':s['text'],'wav':record['wav'],
                             'start_sample':t['start_sample'],'end_sample':t['end_sample'],'frames':n,
                             'full_payload_exact_at_declared_interval':exact,
                             'all_exact_frame_aligned_occurrences_start_samples':positions,
                             'pcm_sha256':digest(pcm),'peak_pcm16':peak,
                             'rms_pcm16':float(np.sqrt(np.mean(values.astype(np.float64)**2)))})
        for name,phoneme in [('Taeo','tˈeɪoʊ'),('Nib','nɪb')]:
            count=len(re.findall(r'\b'+name+r'\b',s['text']))
            if count:
                ph_count=record.get('phonemes','').count(phoneme)
                require(ph_count==count,f'{id_}: {name} input phoneme occurrences differ')
                name_evidence.append({'id':id_,'name':name,'source_occurrences':count,
                                      'recorded_phoneme_input':record['phonemes'],
                                      'expected_phoneme':phoneme,'phoneme_occurrences':ph_count,
                                      'evidence_type':'TTS input metadata; not auditory or recognition evidence'})
    # Reconstruct the policy directly from approved source panels and measured
    # payloads, without importing or executing the narration assembly builder.
    pacing=timing['pacing'];cursor=0;chunks=[];policy_events=[];expected_starts={}
    def hold(seconds,kind,panel=None):
        nonlocal cursor
        n=round(seconds*rate)
        chunks.append(bytes(n*2))
        policy_events.append({'kind':kind,'panel':panel,'start_sample':cursor,'end_sample':cursor+n,'frames':n,'zero_samples_verified':None})
        cursor+=n
    for panel in source['panels']:
        pn=panel['panel']
        voiced_items=[(i,item) for i,item in enumerate(panel['items'],1) if item['kind']=='dialogue']
        hold(pacing.get('dialogue_lead_seconds',pacing['intro_seconds']),'panel_lead',pn)
        if not voiced_items:
            seconds=pacing.get('silent_panel_holds',{}).get(str(pn),pacing['silent_panel_seconds'])
            hold(seconds,'silent_panel_hold',pn)
        else:
            for ordinal,(i,item) in enumerate(voiced_items,1):
                id_=f'p{pn:03d}_l{i:02d}';pcm=payloads[id_]
                expected_starts[id_]=cursor
                require(cursor==by_time[id_]['start_sample'],f'{id_}: start is inconsistent with declared pacing policy')
                chunks.append(pcm);cursor+=len(pcm)//2
                require(cursor==by_time[id_]['end_sample'],f'{id_}: end is inconsistent with declared pacing policy')
                hold(pacing['line_gap_seconds'] if ordinal<len(voiced_items) else pacing.get('panel_tail_seconds',pacing['panel_gap_seconds']),
                     'inter_line_gap' if ordinal<len(voiced_items) else 'panel_tail',pn)
        extra_visual_hold=pacing.get('panel_extra_visual_hold_seconds',{}).get(str(pn),0)
        if extra_visual_hold:
            hold(extra_visual_hold,'extra_visual_reading_hold',pn)
        hold(pacing['panel_gap_seconds'],'panel_transition',pn)
    hold(pacing['outro_seconds'],'outro')
    reconstructed=b''.join(chunks)
    require(reconstructed==assembled,'Full independently reconstructed PCM differs from assembled PCM')
    require(cursor==metadata['frames']==timing['duration_samples'],'Pacing/payload reconstruction total differs')
    for event in policy_events:
        interval=assembled[event['start_sample']*2:event['end_sample']*2]
        event['zero_samples_verified']=not any(interval)
        require(event['zero_samples_verified'],f'Nonzero data in intended {event["kind"]} at sample {event["start_sample"]}')
    gaps=[];last=0
    for t in timing['lines']:
        require(t['start_sample']>=last,f'{t["id"]}: recording overlaps its predecessor')
        if t['start_sample']>last:
            gaps.append({'start_sample':last,'end_sample':t['start_sample'],'frames':t['start_sample']-last,'all_zero':not any(assembled[last*2:t['start_sample']*2])})
        last=t['end_sample']
    if last<metadata['frames']:
        gaps.append({'start_sample':last,'end_sample':metadata['frames'],'frames':metadata['frames']-last,'all_zero':not any(assembled[last*2:])})
    require(all(g['all_zero'] for g in gaps),'Interstitial complement contains nonzero samples')
    decoded=subprocess.run(['ffmpeg','-v','error','-nostdin','-i',str(paths['encoded_mp3']),'-map','0:a:0','-f','s16le','-acodec','pcm_s16le','-ar',str(rate),'-ac','1','pipe:1'],check=True,capture_output=True)
    decoded_pcm=decoded.stdout
    decoded_frames=len(decoded_pcm)//2
    require(len(decoded_pcm)%2==0 and decoded_frames==metadata['frames'],'Decoded gapless MP3 sample framecount differs from PCM master')
    probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(paths['encoded_mp3'])],text=True))
    codec_metrics=signal_metrics(assembled,decoded_pcm)
    speech_frames=sum(r['frames'] for r in line_results)
    silence_frames=sum(g['frames'] for g in gaps)
    unique_payloads=len({digest(pcm) for pcm in payloads.values()})
    require(unique_payloads==56,'Per-line normalized payloads are not all distinct; occurrence interpretation needs duplicate-group accounting')
    synthesis=paths['synthesis_code'].read_text()
    phoneme_call_present='is_phonemes=True' in synthesis
    require(phoneme_call_present,'Synthesis code does not declare direct phoneme input mode')
    report={
        'status':'pass' if not errors else 'fail',
        'scope':'Independent exact PCM assembly audit, approved-source input matching, and actual MP3 decoding; no listening or ASR claims',
        'inputs':inputs,'wav_format':metadata,
        'counts':{'approved_source_dialogue_records':len(source_lines),'recordings':len(recordings),
                  'unique_normalized_pcm_payloads':unique_payloads,'sample_exact_declared_line_intervals':sum(r['full_payload_exact_at_declared_interval'] for r in line_results),
                  'exact_once_payload_occurrence_checks':sum(r['all_exact_frame_aligned_occurrences_start_samples']==[r['start_sample']] for r in line_results),
                  'intended_zero_hold_events':len(policy_events),'interstitial_zero_intervals':len(gaps),
                  'assembled_sample_frames':metadata['frames'],'speech_sample_frames':speech_frames,
                  'interstitial_zero_sample_frames':silence_frames,'decoded_mp3_sample_frames':decoded_frames},
        'duration_seconds':metadata['frames']/rate,'speech_seconds':speech_frames/rate,'interstitial_hold_seconds':silence_frames/rate,
        'all_source_text_and_speaker_metadata_exact':not any('source' in e for e in errors),
        'all_pacing_reconstructed_sample_positions_exact':all(expected_starts[r['id']]==r['start_sample'] for r in line_results),
        'independently_reconstructed_full_pcm_sha256':digest(reconstructed),
        'assembled_pcm_sha256':digest(assembled),
        'full_pcm_reconstruction_matches':reconstructed==assembled,
        'all_interstitial_samples_intended_zero':all(g['all_zero'] for g in gaps),
        'name_phoneme_input_evidence':{'overrides':{'Taeo':'tˈeɪoʊ','Nib':'nɪb'},'direct_phoneme_input_mode_declared':phoneme_call_present,'records':name_evidence,
                                       'claim_limit':'These are exact synthesis inputs. They cannot establish what is audibly spoken or how a name sounds.'},
        'mp3':{'decoded_sample_frames':decoded_frames,'decoder_stderr':decoded.stderr.decode(),
               'decoded_framecount_matches_pcm_master':decoded_frames==metadata['frames'],
               'waveform_metrics_not_recognition':codec_metrics,
               'container_duration_seconds':float(probe['format']['duration']),
               'codec':probe['streams'][0]['codec_name'],'sample_rate':int(probe['streams'][0]['sample_rate']),
               'channels':probe['streams'][0]['channels'],
               'container_duration_note':'MP3 frame padding makes ffprobe container duration differ from the gapless decoded PCM and browser duration; the decoded sample count is the timing check.'},
        'per_recording':line_results,'intended_zero_holds':policy_events,'interstitial_complement':gaps,
        'capability_assessment':{'native_browser_playback':'Confirmed by separate browser integration QA; Chromium decoded audio and advanced its native media clock.',
                                 'subjective_listening':'Not available/performed in this audit; no audio input/listening tool was exposed.',
                                 'transcription':'No callable transcription app exposed. Parent is independently running local recognition; this audit does not perform recognition.'},
        'limitations':[
            'Exact byte inclusion proves every complete normalized line recording was assembled once in source order. It cannot prove that synthesis rendered every word correctly within an individual recording.',
            'Source text, cast and phoneme comparisons validate declared inputs, not perceived voice identity, name pronunciation, emotion or performance.',
            'MP3 is lossy: its decoded PCM is not expected to match master bytes. Matching gapless sample count and waveform similarity establish codec integrity/alignment, not semantic correctness.',
            'No subjective listening took place. Automated recognition elsewhere must be described as recognition, not heard evidence.',
        ],'errors':errors,
    }
    target=OUT/'pcm_timeline_audit.json'
    target.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':report['status'],'counts':report['counts'],'duration_seconds':report['duration_seconds'],
                      'speech_seconds':report['speech_seconds'],'hold_seconds':report['interstitial_hold_seconds'],
                      'mp3_waveform_metrics':codec_metrics,'errors':errors,'output':str(target)},indent=2))
    return 0 if not errors else 1


if __name__=='__main__':
    raise SystemExit(main())
