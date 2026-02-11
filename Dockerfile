# Hafif bir Python imajı kullan
FROM python:3.10-slim

# Çalışma dizinini ayarla
WORKDIR /app

# Gereksinimleri kopyala ve kur
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Proje kodlarını kopyala
COPY . .

# Portu dışa aç
EXPOSE 5000

# Uygulamayı başlat
CMD ["python", "run.py"]