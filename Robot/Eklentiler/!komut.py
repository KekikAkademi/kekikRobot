# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Robot.Edevat.zenginLog import log_yolla, hata_log
from Robot import DESTEK_KOMUT
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
from pyrogram.types import Message
from Robot.Edevat._pyrogram.pyro_yardimcilari import yanitlanan_mesaj

@Client.on_message(filters.command(['komut'], ['!','.','/']))
async def komut(client:Client, message:Message):
    # < Başlangıç
    await log_yolla(client, message)
    yanit_id  = await yanitlanan_mesaj(message)
    ilk_mesaj = await message.reply("__Bekleyin..__",
        reply_to_message_id      = yanit_id,
        disable_web_page_preview = True
    )
    #------------------------------------------------------------- Başlangıç >


    await ilk_mesaj.edit("Merhaba dünyalı")

    try:
        hata_denemesi()
    except Exception as hata:
        await hata_log(hata, client, ilk_mesaj)