# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import json, datetime, pytz
from rich.console import Console

konsol = Console(log_path=False)

def hata(yazi):
   konsol.print(yazi, style="bold red")
def bilgi(yazi):
   konsol.print(yazi, style="blue")
def basarili(yazi):
   konsol.print(yazi, style="bold green")
def onemli(yazi):
   konsol.print(yazi, style="bold cyan")
def soru(soru):
   return konsol.input(f"[bold yellow]{soru}[/]")
def logVer(bisi):
    konsol.log(bisi)

tarih   = lambda : datetime.datetime.now(pytz.timezone("Turkey")).strftime("%d-%m-%Y")
saat    = lambda : datetime.datetime.now(pytz.timezone("Turkey")).strftime("%H:%M:%S")

bilgiler = json.load(open("bilgiler.json"))

async def logYolla(client, message, hata=None):
    # < LOG Alanı
    log_dosya = f"[{saat()} | {tarih()}] "
    sohbet = await client.get_chat(message.chat.id)

    if message.from_user.username:
        log_mesaj   = f"@{message.from_user.username}"
        log_konsol  = f"[bold red]{message.from_user.username}[/] [green]||[/] "
        log_dosya  += f"{message.from_user.username} : "
    else:
        log_mesaj   = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
        log_konsol  = f"[bold red]{message.from_user.first_name}[/] "
        log_dosya   = f"{message.from_user.first_name} "

    if message.chat.type in ['private', 'bot']:
        log_mesaj   += f"\n\n\t\t`{message.text}` __yolladı..__"
        log_konsol  += f"[yellow]{message.text}[/] "
        log_dosya   += f"{message.text} "

    else:
        log_mesaj   += f"\n\n\t\t`{sohbet.title}`__'den__ \n\n\t`{message.text}` __yolladı..__"
        log_konsol  += f"[yellow]{message.text}[/]\t[green]||[/] [bold cyan]{sohbet.title}[/] "
        log_dosya   += f"{message.text} : {sohbet.title} "
    log_mesaj   +=  f"\n\n**Sohbet Türü :** __{message.chat.type}__"
    log_konsol  += f"  [green]||[/] [magenta]{message.chat.type}[/]"
    log_dosya   += f"\t: {message.chat.type}\n"

    if hata:
        log_mesaj   +=  f"\n\n**Hata Türü :** __{hata}__"
        log_konsol  += f"\t[blink magenta]||[/] [bold red]{hata}[/]"
        log_dosya   += f"\n\t\t\t{hata}\n\n"

    await client.send_message(bilgiler['log_id'], log_mesaj)                  # log_id'ye log gönder
    logVer(f"{log_konsol}")                                                   # zenginKonsol'a log gönder

    with open(f"@{bilgiler['session']}.log", "a+") as log_yaz:                 # dosyaya log yaz
        log_yaz.write(log_dosya)
    #-------------------------------------------------------------- Log Alanı >

async def hataLog(client, message, hata_soyle=None):
    # < LOG Alanı
    hata_mesaj   =  f"\n\n**Hata Var !** __{hata_soyle}__"
    hata_konsol  = f"\t\t[bold magenta]||[/] [bold grey74]{hata_soyle}[/]"
    hata_dosya   = f"\n\t\t\t\t\t{hata_soyle}\n\n"

    await client.send_message(bilgiler['log_id'], hata_mesaj)                  # log_id'ye log gönder
    logVer(f"{hata_konsol}")                                                   # zenginKonsol'a log gönder

    with open(f"@{bilgiler['session']}.log", "a+") as log_yaz:                 # dosyaya log yaz
        log_yaz.write(hata_dosya)
    #-------------------------------------------------------------- Log Alanı >
