from flask import Flask, request, jsonify

app = Flask(__name__)

topics = {}
news = [
    {"id": 1, "title": "Latest AI News", "topic": "AI"},
    {"id": 2, "title": "Cloud News", "topic": "Cloud"},
    {"id": 3, "title": "Robotics Innovation", "topic": "AI"}
]

@app.route("/api/news/search")
def search():
    q = request.args.get("q", "").lower()
    results = [
        article for article in news
        if q in article["title"].lower() or q in article["topic"].lower()
    ]
    return jsonify(results), 200

@app.route("/api/articles/<int:article_id>")
def article(article_id):
    result = next((item for item in news if item["id"] == article_id), None)
    if result is None:
        return jsonify({"error": "Article not found"}), 404
    return jsonify(result), 200

@app.route("/api/users/<int:user_id>/topics", methods=["POST"])
def follow_topic(user_id):
    data = request.get_json(silent=True) or {}
    topic = data.get("topic", "").strip()

    if not topic:
        return jsonify({"error": "Topic required"}), 400

    user_topics = topics.setdefault(user_id, set())
    if topic in user_topics:
        return jsonify({"error": "Topic already followed"}), 409

    user_topics.add(topic)
    return jsonify({
        "user_id": user_id,
        "topic": topic,
        "message": "Topic followed successfully"
    }), 201

@app.route("/api/users/<int:user_id>/feed")
def personalized_feed(user_id):
    user_topics = topics.get(user_id, set())
    results = [item for item in news if item["topic"] in user_topics]
    return jsonify(results), 200

@app.route("/api/news/trending")
def trending_news():
    return jsonify(news[:3]), 200

if __name__ == "__main__":
    app.run(debug=True)
