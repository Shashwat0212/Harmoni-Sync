from langdetect import detect
from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")

label_map = {
    "LABEL_0": "Negative",
    "LABEL_1": "Positive",
    "LABEL_2": "Neutral"
}

def detect_language(text):
    try:
        return detect(text) if len(text.strip()) > 10 else "unknown"
    except:
        return "unknown"

def detect_sentiment(text):
    try:
        result = sentiment_pipeline(text[:512])[0]
        return {"label": label_map.get(result['label'], result['label']), "score": round(result['score'], 3)}
    except:
        return {"label": "unknown", "score": 0.0}

def refine_mood(mood_dsp, sentiment):
    if not sentiment or sentiment['label'] == 'unknown':
        return mood_dsp

    sentiment_label = sentiment['label'].lower()

    if mood_dsp == "Happy" and sentiment_label == "negative":
        return "Bittersweet"
    elif mood_dsp in ["Sad", "Depression"] and sentiment_label == "positive":
        return "Uplifting"
    elif sentiment_label == "positive":
        return "Joyous"
    elif sentiment_label == "negative":
        return "Heartbroken"
    else:
        return mood_dsp
