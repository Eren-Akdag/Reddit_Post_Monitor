# Flask ile API oluşturan bir dosya

# Flask kütüphanesini içe aktarın
from flask import Flask, jsonify

# app paketinden app uygulamasını ve reddit modülünü içe aktarın
from app import app, reddit

# API rotası tanımlayın
@app.route("/api/posts")
def api_posts():
    # Postları alın
    posts = reddit.get_posts()
    # Postları JSON formatında döndürün
    return jsonify(posts)
