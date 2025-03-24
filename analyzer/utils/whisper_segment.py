import librosa
import numpy as np
import tensorflow as tf
import soundfile as sf
import whisper

# Load Whisper model
whisper_model = whisper.load_model("base")

# YAMNet setup
YAMNET_MODEL_PATH = "yamnet/yamnet.tflite"
YAMNET_LABELS_PATH = "yamnet/yamnet_class_map.csv"

yamnet_interpreter = tf.lite.Interpreter(model_path=YAMNET_MODEL_PATH)
yamnet_interpreter.allocate_tensors()
input_details = yamnet_interpreter.get_input_details()
output_details = yamnet_interpreter.get_output_details()
yamnet_labels = [line.strip().split(',')[-1] for line in open(YAMNET_LABELS_PATH).readlines()]

def run_yamnet(audio_segment, sr):
    y = librosa.resample(audio_segment, orig_sr=sr, target_sr=16000)
    y = y[:15600]  # YAMNet expects ~0.975 seconds
    input_data = y.astype(np.float32)
    yamnet_interpreter.set_tensor(input_details[0]['index'], input_data)
    yamnet_interpreter.invoke()
    scores = yamnet_interpreter.get_tensor(output_details[0]['index'])[0]
    top_idx = np.argmax(scores)
    label = yamnet_labels[top_idx]
    confidence = scores[top_idx]
    return label, confidence

def split_audio(filepath, sr, duration, chunks=5):
    y, _ = librosa.load(filepath, sr=sr)
    segment_duration = duration / chunks
    return [y[int(i * segment_duration * sr):int((i + 1) * segment_duration * sr)] for i in range(chunks)]

def transcribe_segment(segment, sr):
    temp_path = "temp.wav"
    sf.write(temp_path, segment, sr)
    result = whisper_model.transcribe(temp_path)
    return result["text"]
