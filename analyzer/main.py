from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Create a folder to store uploaded files
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/analyze", methods=["POST"])
def analyze():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # Simulated metadata (we'll later replace this with real analysis)
    metadata = {
        "title": file.filename,
        "bpm": 128,
        "key": "8B",
        "artist": "Unknown",
        "genre": "EDM",
        "length": 213,         # in seconds
        "mood": "joyous"
    }

    return jsonify(metadata), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)
