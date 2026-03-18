from flask import Flask , render_template, request
from EmotionDetection.emotion_detection import emotion_detection
app = Flask(__name__)

@app.route("/emotionDetector")
def detect_emotion():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detection(text_to_analyze)

    anger_score = response.get('anger')
    disgust_score = response.get('disgust')
    fear_score = response.get('fear')
    joy_score = response.get('joy')
    sadness_score = response.get('sadness')
    dominant_emotion = response.get('dominant_emotion')

    return (
        f"For the given statement, the system response is 'anger' : {anger_score}, 'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} and 'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}"
    )

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=5000)