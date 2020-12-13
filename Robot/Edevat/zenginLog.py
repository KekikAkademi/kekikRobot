# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client
from pyrogram.types import Message
import datetime, pytz
from Robot import SESSION_ADI, LOG_ID, hata, taban

tarih   = lambda : datetime.datetime.now(pytz.timezone("Turkey")).strftime("%d-%m-%Y")
saat    = lambda : datetime.datetime.now(pytz.timezone("Turkey")).strftime("%H:%M:%S")

async def log_yolla(client:Client, message:Message):
    ad          = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
    komut       = message.text

    if message.chat.type not in ['private', 'bot']:
        sohbet      = await client.get_chat(message.chat.id)
        sohbet_adi  = f'@{sohbet.username}' if sohbet.username else sohbet.title
    else:
        sohbet_adi  = message.chat.type

    taban.log_salla(ad, komut, sohbet_adi)

    with open(f"@{SESSION_ADI}.log", "a+") as log_yaz:
        log_yaz.write(f'[{saat()} | {tarih()}]' + ' {:20} || {:50} {:>2}|| {:^20}\n'.format(ad, komut, "", sohbet_adi))

    if not ad.startswith("@"):
        ad = f"[{ad}](tg://user?id={message.from_user.id})"

    try:
        await client.send_message(int(LOG_ID), f"**Kullanıcı :** __{ad}__\n\n**Komut :** `{komut}`\n\n**Sohbet :** __{sohbet_adi}__")
    except ValueError:
        hata("\n\tLOG ID Geçersiz..\n")
        await message.reply('`LOG ID geçersiz olduğu için bot kapatıldı!`')
        quit(1)

async def hata_log(hata_:Exception, client:Client, message:Message) -> None:
    taban.hata_salla(hata_)
    await message.edit(f'**Hata Var !**\n\n`{type(hata_).__name__}`\n\n__{hata_}__')

    with open(f"@{SESSION_ADI}.log", "a+") as log_yaz:
        log_yaz.write(f"\n\t\t{type(hata_).__name__}\t»\t{hata_}\n\n")

    try:
        await client.send_message(int(LOG_ID), f'**Hata Var !**\n\n`{type(hata_).__name__}`\n\n__{hata_}__')
    except ValueError:
        hata("\n\tLOG ID Geçersiz..\n")
        await message.reply('`LOG ID geçersiz olduğu için bot kapatıldı!`')
        quit(1)