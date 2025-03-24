# DSP-based mood classification for Indian music context
def classify_mood_india(pitch, timbre, intensity, bpm):
    mood_scores = {
        "Happy": 0,
        "Calm": 0,
        "Sad": 0,
        "Spiritual": 0,
        "Energetic": 0,
        "Bittersweet": 0,
        "Neutral": 0
    }

    # Feature ranges per mood (India-centric)
    ranges = {
        "Happy": {
            "pitch": (700, 2000),
            "bpm": (90, 160),
            "intensity": (0.12, 0.35),
            "zcr": (0.08, 0.20)
        },
        "Calm": {
            "pitch": (200, 800),
            "bpm": (60, 100),
            "intensity": (0.05, 0.15),
            "zcr": (0.03, 0.12)
        },
        "Sad": {
            "pitch": (150, 600),
            "bpm": (40, 90),
            "intensity": (0.04, 0.12),
            "zcr": (0.02, 0.08)
        },
        "Spiritual": {
            "pitch": (250, 900),
            "bpm": (60, 120),
            "intensity": (0.10, 0.3),
            "zcr": (0.05, 0.15)
        },
        "Energetic": {
            "pitch": (600, 1500),
            "bpm": (120, 200),
            "intensity": (0.20, 0.50),
            "zcr": (0.10, 0.25)
        }
    }

    for mood, feats in ranges.items():
        if feats["pitch"][0] <= pitch <= feats["pitch"][1]:
            mood_scores[mood] += 1
        if feats["bpm"][0] <= bpm <= feats["bpm"][1]:
            mood_scores[mood] += 1
        if feats["intensity"][0] <= intensity <= feats["intensity"][1]:
            mood_scores[mood] += 1
        if feats["zcr"][0] <= timbre[0] <= feats["zcr"][1]:
            mood_scores[mood] += 1

    top_mood = max(mood_scores, key=mood_scores.get)
    return top_mood if mood_scores[top_mood] > 1 else "Neutral"
