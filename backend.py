from flask import Flask, request, jsonify
from database.emotion_store import save_emotion
from database.emotion_store import save_emotion, get_emotion_heatmap

app = Flask(__name__)

@app.route('/api/save_emotion', methods=['POST'])
def record_emotion():
    data = request.json
    user_id = data.get('user_id')
    emotion = data.get('emotion')
    confidence = data.get('confidence')
    
    if not all([user_id, emotion, confidence]):
        return jsonify({"error": "Missing fields"}), 400

    result = save_emotion(user_id, emotion, confidence)
    return jsonify(result), 200


@app.route('/api/heatmap/<user_id>', methods=['GET'])
def get_heatmap(user_id):
    result = get_emotion_heatmap(user_id)
    return jsonify(result), 200


if __name__ == "__main__":
    app.run(debug=True)
