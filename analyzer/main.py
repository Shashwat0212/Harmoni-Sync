from flask import Flask, request, jsonify
import os
import eyed3
import librosa
from utils.feature_extraction import estimate_key, extract_pitch, extract_rms_intensity, extract_timbre
from utils.whisper_segment import run_yamnet, split_audio, transcribe_segment
from utils.sentiment import detect_language, detect_sentiment, refine_mood
from mood_engines.india_engine import classify_mood_india

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/analyze", methods=["POST"])
def analyze():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    try:
        y, sr = librosa.load(filepath, mono=True)
        bpm, _ = librosa.beat.beat_track(y=y, sr=sr)
        bpm = int(bpm.item() if hasattr(bpm, "item") else bpm)
        key = estimate_key(y, sr)
        duration = librosa.get_duration(y=y, sr=sr)

        audiofile = eyed3.load(filepath)
        artist = audiofile.tag.artist if audiofile and audiofile.tag and audiofile.tag.artist else "Unknown"

        pitch = extract_pitch(y, sr)
        intensity = extract_rms_intensity(y)
        timbre = extract_timbre(y, sr)

        mood_dsp = classify_mood_india(pitch, timbre, intensity, bpm)

        segments = split_audio(filepath, sr, duration)
        lyrics = ""
        vocals_found = False

        for segment in segments:
            label, confidence = run_yamnet(segment, sr)
            if any(x in label.lower() for x in ["speech", "singing", "vocal"]) and confidence > 0.5:
                vocals_found = True
                lyrics = transcribe_segment(segment, sr)
                if len(lyrics.strip()) > 10:
                    break

        language = detect_language(lyrics) if vocals_found else "unknown"
        sentiment = detect_sentiment(lyrics) if vocals_found else None
        final_mood = refine_mood(mood_dsp, sentiment)

        return jsonify({
            "artist": artist,
            "bpm": bpm,
            "key": key,
            "language": language,
            "mood": final_mood
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)
