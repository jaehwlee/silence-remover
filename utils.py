import numpy as np
import librosa


def remove_silence(audio, top_db=53, frame_length=1024, hop_length=256, skip_idx=0):
    # Trim leading and trailing silence from an audio signal
    _, trim_index = librosa.effects.trim(audio, top_db=20)
    audio =  audio[max(trim_index[0], 0):min(trim_index[1], len(audio))]
    
    # Split an audio signal into non-silent intervals.
    edges = librosa.effects.split(audio,
            top_db=top_db, frame_length=frame_length, hop_length=hop_length)

    trimmed_audio = np.array([])
    
    # Concatenate non-silent signal	
    for idx, (start, end) in enumerate(edges[skip_idx:]):
        # print non-silent interval
        trimmed_audio = np.concatenate((trimmed_audio, audio[start:end]), axis=0)
       
    return trimmed_audio
  

def get_silence(sec):
    return np.zeros(22050 * sec)
  
  
def load_audio(path, pre_silence_length=0, post_silence_length=0):
    audio = librosa.core.load(path, sr=22050)[0]
    if pre_silence_length > 0 or post_silence_length > 0:
        audio = np.concatenate([
                get_silence(pre_silence_length),
                audio,
                get_silence(post_silence_length),
        ])
	
    return audio
