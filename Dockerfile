# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

# Docker Python İmajı
FROM python:3.9.5-buster

RUN apt-get update && apt-get upgrade -y

# Gerekli Paketlerin Yüklenmesi
RUN apt-get install -y ffmpeg python3-pip opus-tools

# Pip Güncellemesi
RUN python3.9 -m pip install -U pip

COPY . .

RUN python3.9 -m pip install -Ur requirements.txt

# Botun Başlatılması
CMD ["python3.9","basla.py"]