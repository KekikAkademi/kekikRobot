# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from roBot.Edevat import konsol, basarili
from roBot.Nitelik import *

from pyrogram import Client, filters
from pyrogram import __version__
import sys, json
from os import listdir


bilgiler = json.load(open("bilgiler.json"))

kekikRobot          = Client(
    api_id          = bilgiler['api_id'],                   # my.telegram.org/apps
    api_hash        = bilgiler['api_hash'],                 # my.telegram.org/apps
    session_name    = f"@{bilgiler['session']}",            # Fark Etmez
    bot_token       = bilgiler['bot_token'],                # @BotFather
    plugins         = dict(root="roBot/Eklentiler")
)

tum_eklentiler = []
for dosya in listdir("./roBot/Eklentiler/"):
    if not dosya.endswith(".py") or dosya.endswith("__.py"):
        continue
    tum_eklentiler.append(f"📂 {dosya.replace('.py','')}")

def baslangic():
    kekikRobot.start()

    surum = f"{str(sys.version_info[0])}.{str(sys.version_info[1])}"
    konsol.print(f"\t\t[gold1]@{bilgiler['session']}[/] [yellow]:bird:[/] [bold red]Python: [/][i]{surum}[/]")
    basarili(f"  {bilgiler['session']} [magenta]v[/] [blue]{__version__}[/] [red]Pyrogram[/] tabanında [magenta]{len(tum_eklentiler)} eklentiyle[/] çalışıyor...\n")
    
    kekikRobot.stop()