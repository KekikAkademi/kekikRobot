# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from roBot import logYolla, hataLog, DESTEK_KOMUT
from pathlib import Path

DESTEK_KOMUT.update({
    Path(__file__).stem : {
        "aciklama"  : "Merhaba dünya..",
        "kullanim"  : [
            None
            ],
        "ornekler"  : [
            ".komut"
            ]
    }
})

from pyrogram import Client, filters
from roBot.Edevat._from_nana.pyro_yardimcilari import ReplyCheck
import json

bilgiler = json.load(open("bilgiler.json"))

@Client.on_message(filters.command(['komut'], ['!','.','/']))
async def komut(client, message):
    # < Başlangıç
    await logYolla(client, message)
    yanitlanacak_mesaj = ReplyCheck(message)
    ilk_mesaj = await message.reply("__Bekleyin..__",
        reply_to_message_id         = yanitlanacak_mesaj,
        disable_web_page_preview    = True,
        parse_mode                  = "Markdown"
    )
    #------------------------------------------------------------- Başlangıç >

    if message.from_user.id in bilgiler['yetkili']:
        await message.reply("__padişahım çok yaşa__", reply_to_message_id=yanitlanacak_mesaj)
    else:
        await message.reply("Merhaba dünyalı")

    try:
        hata_denemesi()
    except Exception as hata:
        await hataLog(client, message, hata)