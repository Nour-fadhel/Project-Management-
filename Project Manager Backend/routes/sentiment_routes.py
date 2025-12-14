from flask import Blueprint, jsonify
from models.task_model import TaskComment
from services.sentiment_service import analyze_sentiment

sentiment_bp = Blueprint("sentiment", __name__)

@sentiment_bp.route("/task/<int:task_id>", methods=["GET"])
def analyze_task_sentiment(task_id):
    comments = TaskComment.query.filter_by(task_id=task_id).all()

    if not comments:
        return jsonify({"task_id": task_id, "sentiment": "Neutral"})

    text = " ".join([c.content for c in comments if c.content])

    sentiment = analyze_sentiment(text)

    return jsonify({
        "task_id": task_id,
        "sentiment": sentiment
    })
