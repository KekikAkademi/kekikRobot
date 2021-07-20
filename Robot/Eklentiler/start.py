# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Robot.Edevat.zenginLog import log_yolla
from pyrogram import Client, filters
from pyrogram.types import Message

from Robot.Edevat._pyrogram.BUTON_OLUSTURUCU import buton_ver

@Client.on_message(filters.command(['start'], ['!','.','/']) & filters.private)
async def start_buton(client:Client, message:Message):
    # < Başlangıç
    await log_yolla(client, message)

    ilk_mesaj = await message.reply("ℹ️ `Hallediyorum..`",
        quote                    = True,
        disable_web_page_preview = True
    )
    #------------------------------------------------------------- Başlangıç >

    await ilk_mesaj.delete()
    await message.reply("TM", quote = True, reply_markup = buton_ver(["📚 Yardım", "💸 Bağışta Bulun"], 2))