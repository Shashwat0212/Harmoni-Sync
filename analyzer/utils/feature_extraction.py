import numpy as np
import librosa

def estimate_key(y, sr):
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    chroma_mean = np.mean(chroma, axis=1)
    key_index = chroma_mean.argmax()
    camelot_keys = {
        'C': '8B', 'C#': '3B', 'D': '10B', 'D#': '5B', 'E': '12B',
        'F': '7B', 'F#': '2B', 'G': '9B', 'G#': '4B', 'A': '11B',
        'A#': '6B', 'B': '1B'
    }
    keys = list(camelot_keys.keys())
    return camelot_keys[keys[key_index % 12]]

def extract_pitch(y, sr):
    pitches, _ = librosa.piptrack(y=y, sr=sr)
    pitch_values = pitches[pitches > 0]
    return np.mean(pitch_values) if pitch_values.size else 0

def extract_rms_intensity(y):
    rms = librosa.feature.rms(y=y)
    return np.mean(rms)

def extract_timbre(y, sr):
    zcr = librosa.feature.zero_crossing_rate(y)
    spectral_contrast = librosa.feature.spectral_contrast(y=y, sr=sr)
    return np.mean(zcr), np.mean(spectral_contrast)
