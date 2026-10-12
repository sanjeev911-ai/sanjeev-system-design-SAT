from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/news")
def get_news():
    return jsonify({
        "articles": [
            {"id": 1, "title": "Latest AI News"},
            {"id": 2, "title": "Breaking News"}
        ]
    }), 200

@app.route("/api/feed/<int:user_id>")
def personalized_feed(user_id):
    # Sample response for demonstrating the high-level architecture.
    return jsonify({
        "user_id": user_id,
        "feed": ["Latest AI News", "Robotics Innovation"]
    }), 200

@app.route("/api/news/trending")
def trending_news():
    return jsonify({
        "trending": ["AI News", "Technology News"]
    }), 200

if __name__ == "__main__":
    app.run(debug=True)
