from flask import Flask, request, jsonify
import os
import eyed3
import librosa

from utils.feature_extraction import (
    estimate_key,
    extract_pitch,
    extract_rms_intensity,
    extract_timbre,
    detect_genre
)

from utils.whisper_segment import (
    run_yamnet,
    split_audio,
    transcribe_segment
)

from utils.sentiment import (
    detect_language,
    detect_sentiment,
    refine_mood
)

from mood_engines.india_engine import classify_mood_india

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/analyze", methods=["POST"])
def analyze():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    filename = file.filename
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    try:
        # Load audio
        y, sr = librosa.load(filepath, mono=True)
        duration = librosa.get_duration(y=y, sr=sr)
        bpm, _ = librosa.beat.beat_track(y=y, sr=sr)
        bpm = int(bpm.item() if hasattr(bpm, "item") else bpm)
        key = estimate_key(y, sr)

        # Get metadata from file tag
        audiofile = eyed3.load(filepath)
        artist = audiofile.tag.artist if audiofile and audiofile.tag and audiofile.tag.artist else "Unknown"

        # DSP Features
        pitch = extract_pitch(y, sr)
        intensity = extract_rms_intensity(y)
        timbre = extract_timbre(y, sr)

        # Mood from DSP
        mood_dsp = classify_mood_india(pitch, timbre, intensity, bpm)

        # Whisper + Yamnet for sentiment/mood/lyrics
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

        # Genre detection via full-track Yamnet
        genre = detect_genre(filepath)

        return jsonify({
            "title": filename,
            "artist": artist,
            "bpm": bpm,
            "key": key,
            "language": language,
            "mood": final_mood,
            "genre": genre,
            "length": int(duration)
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)
