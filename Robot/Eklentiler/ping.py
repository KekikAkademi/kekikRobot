# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Robot.Edevat.zenginLog import log_yolla, hata_log
from Robot import DESTEK_KOMUT
from pathlib import Path

DESTEK_KOMUT.update({
    Path(__file__).stem : {
        "aciklama"  : "botun hayatta olup olmadığı kontrolü..",
        "kullanim"  : [
            None
            ],
        "ornekler"  : [
            ".ping"
            ]
    }
})

from pyrogram import Client, filters
from pyrogram.types import Message
from Robot.Edevat._pyrogram.pyro_yardimcilari import yanitlanan_mesaj
from Robot import YETKILI
import asyncio, datetime

@Client.on_message(filters.command(['ping'], ['!','.','/']))
async def ping(client:Client, message:Message):
    # < Başlangıç
    await log_yolla(client, message)
    yanit_id  = await yanitlanan_mesaj(message)
    ilk_mesaj = await message.reply("__Bekleyin..__",
        reply_to_message_id      = yanit_id,
        disable_web_page_preview = True
    )
    #------------------------------------------------------------- Başlangıç >

    basla = datetime.datetime.now()

    mesaj = "__Pong!__"

    bitir = datetime.datetime.now()
    sure = (bitir - basla).microseconds
    mesaj += f"\n\n**Tepki Süresi :** `{sure} ms`"

    await ilk_mesaj.edit(mesaj)

    await asyncio.sleep(3)
    await ilk_mesaj.edit("__şimdi mutlu musun?__")
    await asyncio.sleep(1)

    try:
        await ilk_mesaj.edit(mesaj)
    except Exception as hata:
        await hata_log(hata, client, ilk_mesaj)

@Client.on_message(filters.command(['json'], ['!','.','/']))
async def jsn_ver(client:Client, message:Message):
    # < Başlangıç
    await log_yolla(client, message)
    yanit_id  = await yanitlanan_mesaj(message)

    if str(message.from_user.id) not in YETKILI:
        await message.reply("__admin değilmişsin kekkooo__", reply_to_message_id=yanit_id)
        return

    ilk_mesaj = await message.reply("`Hallediyorum..`",
        reply_to_message_id      = yanit_id,
        disable_web_page_preview = True
    )
    #------------------------------------------------------------- Başlangıç >

    await ilk_mesaj.edit(f"```{message.reply_to_message}```")