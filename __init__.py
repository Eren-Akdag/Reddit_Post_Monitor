# app paketini oluşturmak için boş bir __init__.py dosyası yeterlidir

# Flask kütüphanesini içe aktarın
from flask import Flask

# Flask uygulamasını oluşturun
app = Flask(__name__)

# api.py dosyasını içe aktarın
from app import api
