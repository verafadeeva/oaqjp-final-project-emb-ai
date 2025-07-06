"""main flask module."""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector


app = Flask(__name__)

@app.route("/emotionDetector")
def emotion():
    """
    Handles GET requests with a query parameter 'textToAnalyze' containing the text 
    to analyze for emotions.
    """
    text = request.args.get("textToAnalyze", None)
    verdict = emotion_detector(text)

    if verdict["dominant_emotion"] is None:
        return "Invalid text! Please try again!."

    return (f"For the given statement, the system response is 'anger': {verdict['anger']}, "
            f"'disgust': {verdict['disgust']}, 'fear': {verdict['fear']}, "
            f"'joy': {verdict['joy']} and 'sadness': {verdict['sadness']}. "
            f"The dominant emotion is {verdict['dominant_emotion']}."
            )


@app.route("/")
def index():
    """Handles GET requests, root page"""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
