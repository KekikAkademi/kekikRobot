# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from roBot import logYolla, hataLog, DESTEK_KOMUT
from pathlib import Path

DESTEK_KOMUT.update({
    Path(__file__).stem : {
        "aciklama"  : "botun hayatta olup olmadığı kontrolü..",
        "kullanim"  : [
            "mesaj",
            "yanıtlanan mesaj"
            ],
        "ornekler"  : [
            ".ping"
            ]
    }
})

from pyrogram import Client, filters
from roBot.Edevat._from_nana.pyro_yardimcilari import ReplyCheck
import asyncio, datetime

@Client.on_message(filters.command(['ping'], ['!','.','/']))
async def ping(client, message):
    # < Başlangıç
    await logYolla(client, message)
    yanitlanacak_mesaj = ReplyCheck(message)
    ilk_mesaj = await message.reply("__Bekleyin..__",
        reply_to_message_id         = yanitlanacak_mesaj,
        disable_web_page_preview    = True,
        parse_mode                  = "Markdown"
    )
    #------------------------------------------------------------- Başlangıç >

    basla = datetime.datetime.now()
    
    mesaj = "__Pong!__"

    bitir = datetime.datetime.now()
    sure = (bitir - basla).microseconds/10000
    mesaj += f"\n\n**Tepki Süresi :** `{sure} ms`"

    await ilk_mesaj.edit(mesaj)
    
    await asyncio.sleep(3)
    await ilk_mesaj.edit("__şimdi mutlu musun?__")
    await asyncio.sleep(1)

    try:
        await ilk_mesaj.edit(mesaj)
    except Exception as hata:
        await hataLog(client, message, hata)