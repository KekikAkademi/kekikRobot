# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, __version__
from pyrogram.errors import ApiIdInvalid, AccessTokenInvalid
import os, sys
from dotenv import load_dotenv
from KekikTaban import KekikTaban

taban = KekikTaban(
    baslik   = "@KekikAkademi Robot",
    aciklama = "kekikRobot Başlatıldı..",
    banner   = "kekikRobot",
    girinti  = 3
)

konsol = taban.konsol

def hata(yazi:str) -> None:
   konsol.print(yazi, style="bold red")
def bilgi(yazi:str) -> None:
   konsol.print(yazi, style="blue")
def basarili(yazi:str) -> None:
   konsol.print(yazi, style="bold green", width=70, justify="center")
def onemli(yazi:str) -> None:
   konsol.print(yazi, style="bold cyan")

if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    hata("""En az python 3.6 sürümüne sahip olmanız gerekir.
              Birden fazla özellik buna bağlıdır. Bot kapatılıyor.""")
    quit(1)

if (taban.bellenim_surumu.split('-')[-1] != 'aws') and (not os.path.exists("ayar.env")): # Heroku Geçmek için aws
    hata("\n\tLütfen ayar.env dosyanızı oluşturun..\n")
    quit(1)

load_dotenv("ayar.env")

# Yapılandırmanın önceden kullanılan değişkeni kullanarak düzenlenip düzenlenmediğini kontrol edin.
# Temel olarak, yapılandırma dosyası için kontrol.
AYAR_KONTROL = os.environ.get("___________LUTFEN_______BU_____SATIRI_____SILIN__________", None)

if AYAR_KONTROL:
    hata("\n\tLütfen ayar.env dosyanızı düzenlediğinize emin olun /veya\n\tilk hashtag'de belirtilen satırı kaldırın..\n")
    quit(1)

API_ID          = str(os.environ.get("API_ID", str))
API_HASH        = str(os.environ.get("API_HASH", str))
BOT_TOKEN       = str(os.environ.get("BOT_TOKEN", str))
LOG_ID          = str(os.environ.get("LOG_ID", str))
YETKILI         = str(os.environ.get("YETKILI", str)).split(',')
SESSION_ADI     = os.environ.get("SESSION_ADI", "kekikRobot")
INDIRME_ALANI   = os.environ.get("INDIRME_ALANI", "downloads/")
if not os.path.isdir(INDIRME_ALANI): os.makedirs(INDIRME_ALANI)

try:
    kekikRobot          = Client(
        api_id          = API_ID,
        api_hash        = API_HASH,
        session_name    = f'@{SESSION_ADI}',
        bot_token       = BOT_TOKEN,
        plugins         = dict(root="Robot/Eklentiler")
    )
except ValueError:
    hata("\n\tLütfen ayar.env dosyanızı DÜZGÜNCE! oluşturun..\n")
    quit(1)

DESTEK_KOMUT = {}

tum_eklentiler = []
for dosya in os.listdir("./Robot/Eklentiler/"):
    if not dosya.endswith(".py") or dosya.startswith("_"):
        continue
    tum_eklentiler.append(f"📂 {dosya.replace('.py','')}")

def baslangic() -> None:
    try:
        kekikRobot.start()
    except ApiIdInvalid:
        hata('\n\tayar.env dosyasındaki API Bilgileri Geçersiz..\n')
        quit(1)
    except AccessTokenInvalid:
        hata('\n\tBot Token Geçersiz..\n')
        quit(1)

    surum = f"{str(sys.version_info[0])}.{str(sys.version_info[1])}"
    konsol.print(f"[gold1]@{SESSION_ADI}[/] [yellow]:bird:[/] [bold red]Python: [/][i]{surum}[/]", width=70, justify="center")
    basarili(f"{SESSION_ADI} [magenta]v[/] [blue]{__version__}[/] [red]Pyrogram[/] tabanında [magenta]{len(tum_eklentiler)} eklentiyle[/] çalışıyor...\n")

    kekikRobot.stop()
