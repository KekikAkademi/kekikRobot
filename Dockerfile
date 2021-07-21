# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

# Docker Python İmajı
FROM python:3.9.6-slim-buster

WORKDIR /opt/app/KekikRobot
COPY ./ /opt/app/KekikRobot/

# Gerekli Paketlerin Yüklenmesi
RUN apt-get -y update && \
    apt-get install --no-install-recommends -y \
    ffmpeg \
    opus-tools \
    && \
    rm -rf /var/lib/apt/lists/*

# Pip Güncellemesi ve Kütüphane Kurulumları
RUN python3.9 -m pip install -U pip

RUN python3.9 -m pip install --upgrade pip && \
    python3.9 -m pip install --no-cache-dir -Ur requirements.txt

# Botun Başlatılması
CMD ["python3.9", "basla.py"]