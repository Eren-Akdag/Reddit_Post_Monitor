# pytest ile testleri içeren bir dosya

# pytest kütüphanesini içe aktarın
import pytest

# app paketinden reddit modülünü içe aktarın
from app import reddit

# Test fonksiyonlarınızı tanımlayın
# Test fonksiyonlarının adının "test_" ile başlaması gerekiyor

def test_get_posts():
    # get_posts fonksiyonunun doğru şekilde çalıştığını kontrol edin
    # Örneğin, post sayısının 25 olduğunu varsayalım
    posts = reddit.get_posts()
    assert len(posts) == 25
    # Postların başlık, yazar, url ve post_id alanlarına sahip olduğunu kontrol edin
    for post in posts:
        assert "title" in post
        assert "author" in post
        assert "url" in post
        assert "post_id" in post

def test_api_posts():
    # api_posts fonksiyonunun doğru şekilde çalıştığını kontrol edin
    # Örneğin, JSON formatında bir cevap döndürdüğünü varsayalım
    response = reddit.api_posts()
    assert response.is_json
    # Cevabın içindeki postların get_posts ile aynı olduğunu kontrol edin
    posts = reddit.get_posts()
    assert response.get_json() == posts
