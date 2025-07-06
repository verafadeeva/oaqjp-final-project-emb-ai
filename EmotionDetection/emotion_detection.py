import json
import requests


def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, headers=headers, json=data, timeout=6.03)
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    formatted = json.loads(response.text)

    emotions = {
        "anger": formatted["emotionPredictions"][0]["emotion"]["anger"],
        "disgust": formatted["emotionPredictions"][0]["emotion"]["disgust"],
        "fear": formatted["emotionPredictions"][0]["emotion"]["fear"],
        "joy": formatted["emotionPredictions"][0]["emotion"]["joy"],
        "sadness": formatted["emotionPredictions"][0]["emotion"]["sadness"]
    }

    dominant_emotion = None
    max_emotion_score = 0

    for emotion_name, score_value in emotions.items():
        if score_value > max_emotion_score:
            max_emotion_score = score_value
            dominant_emotion = emotion_name
    
    emotions["dominant_emotion"] = dominant_emotion
    return emotions
