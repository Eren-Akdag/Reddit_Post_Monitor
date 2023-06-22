# Bir temel imaj seçin
# Örneğin, Python 3.9 sürümünü içeren bir imaj seçelim
FROM python:3.9

# Çalışma dizinini belirleyin
# Örneğin, /app dizinini seçelim
WORKDIR /app

# Gerekli dosyaları kopyalayın
# Örneğin, app klasörünü ve requirements.txt dosyasını kopyalayalım
COPY app .
COPY requirements.txt .

# Gerekli kütüphaneleri yükleyin
# Örneğin, requirements.txt dosyasındaki kütüphaneleri pip ile yükleyelim
RUN pip install -r requirements.txt

# Uygulamayı çalıştırmak için komut belirleyin
# Örneğin, api.py dosyasını flask ile çalıştıralım
CMD ["flask", "run"]
