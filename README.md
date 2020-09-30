# kekikRobot
[@KekikAkademi](https://t.me/KekikAkademi) *geliştiricileri için*, `Pyrogram` ile yazılmış, *eklenti geliştirilmeye hazır* bir **telegram bot** tabanıdır.

![Buraya görsel gelecek](https://github.com/KekikAkademi/Depo/blob/master/PHP/Botlar/!acz/acz-db-olusturucu/ajax/loading.gif?raw=true)

 - [x] *Konsol tabanı* **»** `konsolTaban/`
 - [x] *Robot tabanı* **»** `roBot/__init__.py`
 - [x] *Log sistemi* **»** `roBot/Edevat/zenginLog.py`
 - [x] *Ana komutlar ve Eklenti destek sistemi* **»** `roBot/Nitelik/ana_komutlar.py`
 - [x] *Eklenti yönetim sistemi* **»** `roBot/Nitelik/eklenti_yonetimi.py`
 - [x] *Ana butonlar* **»** `roBot/Nitelik/ana_butonlar.py`
 - [x] *Pyrogram için çeşitli* <ins>Edevatlar</ins> **»** `roBot/Edevat/_pyrogram/`
	 - [x]  *İndirme/Yükleme için Progress* **»** `roBot/Edevat/_pyrogram/progress.py`
	 - [x] *Pratik bir şekilde buton oluşturucu* **»** `roBot/Edevat/_pyrogram/inline_buton_olusturucu.py`
	 - [x] *[Nana-Remix](https://github.com/pokurt/Nana-Remix)'den çalınan Edevatlar* **»** `roBot/Edevat/_from_nana/`
- [x] *Örnek eklentiler* **»** `roBot/Eklentiler/`

##

1.  **Repo'yu fork edin**  *ve*  **private**  *yapın!*
2. *Repo'nun adını değiştirin.*
3.  **Fork ettiğiniz kendi reponuzu**, *Cihazınıza indirin.*  `bilgiler.json`' u *kendi bilgilerinizle* düzenleyin.. 
	- `api_id` **»**  [my.telegram.org/apps](my.telegram.org/apps)
	- `api_hash` **»**  [my.telegram.org/apps](my.telegram.org/apps)
	- `session` **»**  **Botunuzun İsmi** *(farke tmez)*
	- `bot_token` **»** [@BotFather](https://t.me/BotFather)
	- `log_id` **»** *Anlık logların gönderileceği kanal, grup veya user id*
	- `yetkili` **»** *Sadece yetkili kullanıcıların kullanabileceği komutları filtrelemek için user id* **örn.:** `.logsalla`
4.  **.session** *oluşması için Cihazınızda* `basla.py` *dosyasını çalıştırın ve telegram onayınızı tamamlayın..*
5. `bilgiler.json` *ve* `session` *dosyanız size ait olduktan sonra* *repo'yu push edin..**
6.  *Heroku'da uygulama oluşturun,* **private github reponuzu** *bağlayın ve* **otomatik deployu enable yapıp** deploy edin.
	-  *kendi reponuz'da yaptığınız değişikliği push ettiğiniz anda herokuda otomatik olarak güncelleme çekilip yeniden başlar..*
7.  *Deploy tamamlandıktan sonra resources sekmesine gelip dyno'yu aktive edin.*
8.  *Hayırlı olsun, Telegram'da*  **.yardim**  *komutuyla devam edin..*

##

`roBot/Eklentiler/` dizini altında yeni dosya oluşturup kendi eklentinizi geliştirmenin keyfini çıkarın..
