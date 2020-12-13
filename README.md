# kekikRobot 🤖

[@KekikAkademi](https://t.me/KekikAkademi) *geliştiricileri için*, `Pyrogram` ile yazılmış, *eklenti geliştirilmeye hazır* bir **Telegram Robot** tabanıdır.

![kekikRobot](https://i.imgur.com/DGURnPh.png)

- [x] *Konsol tabanı* **»** `konsolTaban/`
- [x] *Robot tabanı* **»** `Robot/__init__.py`
- [x] *Log sistemi* **»** `Robot/Edevat/zenginLog.py`
- [x] *Ana komutlar ve Eklenti destek sistemi* **»** `Robot/Eklentiler/_ana_komutlar.py`
- [x] *Ana butonlar* **»** `Robot/Eklentiler/_ana_butonlar.py`
- [x] *Eklenti yönetim sistemi* **»** `Robot/Eklentiler/_eklenti_yonetimi.py`
- [x] *Pyrogram için çeşitli* <ins>Edevatlar</ins> **»** `Robot/Edevat/_pyrogram/`
- [x] *Örnek eklentiler* **»** `Robot/Eklentiler/`

##

- Repo'yu _Fork Edin_ ve Cihazınıza **Kendi Reponuzu** indirin..
- Aşağıdaki `Heroku Deploy` butonuna basın.
- _Heroku Deploy_ aşamasını tamamlayın.
- Oluşturduğunuz uygulamanın `Deploy` sekmesinden **kendi github reponuzu bağlayın** ve **otomatik deployu enable edin**
  - __kendi reponuz'da yaptığınız değişikliği push ettiğiniz anda herokuda otomatik olarak güncelleme çekilip yeniden başlar..__
- `Robot/Eklentiler/` dizini altında yeni dosya oluşturup kendi eklentinizi geliştirmenin keyfini çıkarın..

##

# 🤖 kekikRobot

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/ef21dc5020ff4c1690ef9d0e847c67c0)](https://www.codacy.com/gh/KekikAkademi/kekikRobot/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=KekikAkademi/kekikRobot&amp;utm_campaign=Badge_Grade) ![Repo Boyutu](https://img.shields.io/github/repo-size/KekikAkademi/kekikRobot) ![Views](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https://github.com/KekikAkademi/kekikRobot&title=Profile%20Views) [![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/KekikAkademi/kekikRobot)

[Pyrogram](https://github.com/pyrogram/pyrogram) *kullanılarak oluşturulmuş* **Telegram Robot** *geliştirme tabanı.*

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/keyiflerolsun/)

## :rocket: Deploy Edin

### HEROKU ie Deploy Edin

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/KekikAkademi/kekikRobot)

### Elle Deploy Edin

1. Depoyu klonlayın,
2. `ayar.env` dosyasını kendinize göre düzenleyin,
3. `basla.py` betiğini çalıştırın;

```sh
git clone https://github.com/KekikAkademi/kekikRobot.git
cd kekikRobot
cp _ornek_ayar.env ayar.env && nano ayar.env

        # Virtualenv fetişiniz varsa kullanabilirsiniz..
        pip install virtualenv
        virtualenv -p /usr/bin/python3 venv
        . ./venv/bin/activate

# Eğer yoksa direk bu satıra atlayabilirsiniz..
pip install -r requirements.txt
python3 basla.py
```

## :green_heart: Özel Teşekkürler

* **Bir çok şey için** [By_Azade](https://github.com/muhammedfurkan) 🕊
* [TeleRobot](https://github.com/ynsmrkrblt/TeleRobot) **için** [ynsmrkrblt](https://github.com/ynsmrkrblt) 🕊
* [TelePyroBot](https://github.com/SkuzzyxD/TelePyroBot) **için** [SkuzzyxD](https://github.com/SkuzzyxD) 🕊
* [Nana-Remix](https://github.com/pokurt/Nana-Remix) **için** [pokurt](https://github.com/pokurt) 🕊
* [AsenaRobot](https://github.com/Quiec/AsenaRobot) **için** [Quiec](https://github.com/Quiec) 🕊

## :globe_with_meridians: Telif Hakkı ve Lisans

* *Copyright (C) 2020 by* [keyiflerolsun](https://github.com/keyiflerolsun) ❤️️
* [GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007](https://github.com/KekikAkademi/kekikRobot/blob/master/LICENSE) *Koşullarına göre lisanslanmıştır..*

## :recycle: İletişim

*Benimle iletişime geçmek isterseniz, **Telegram**'dan mesaj göndermekten çekinmeyin;* [@keyiflerolsun](https://t.me/keyiflerolsun)

##

> **[@KekikAkademi](https://t.me/KekikAkademi)** *için yazılmıştır..*