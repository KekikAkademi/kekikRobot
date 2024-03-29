# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Robot.Edevat.zenginLog import log_yolla, hata_log
from Robot import DESTEK_KOMUT
from pathlib import Path

DESTEK_KOMUT.update({
    Path(__file__).stem : {
        "aciklama" : "Bir takım buton oluşturma denemeleri",
        "kullanim" : [
            "buton_olustur(butonlar=dict, adet=3, link=True)",
            "buton_olustur(butonlar=dict, adet=2, link=True, geri='geri_don')",
            "buton_olustur(butonlar=dict, adet=2, data=True, ana_Sayfa='ana_Sayfa')",
            ],
        "ornekler" : [
            ".kimo"
            ]
    }
})

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, CallbackQuery
import asyncio
from Robot.Edevat._pyrogram.BUTON_OLUSTURUCU import buton_olustur
# buton_olustur(butonlar=dict, adet=3, link=True)

@Client.on_message(filters.command(['buton'], ['!','.','/']))
async def buton(client:Client, message:Message):
    # < Başlangıç
    await log_yolla(client, message)
    #------------------------------------------------------------- Başlangıç >

    butonlar = {
        "Beni Yazan" : "t.me/keyiflerolsun",
        "Kekik"      : "t.me/KekikAkademi"
    }

    linkli_butonlar = buton_olustur(butonlar=butonlar, adet=2, link=True, ana_sayfa='🏘 Ana Sayfa')
    await message.reply(
        "Bunu yazan tosun\n\tokuyana Kekik",
        reply_markup=InlineKeyboardMarkup(linkli_butonlar)
    )

    await asyncio.sleep(2)

    data_butonlar = buton_olustur(butonlar=butonlar, adet=2, data=True, geri='📚 Yardım')
    await message.reply(
        "`yardim` ve `ana_sayfa` dataları `Robot/Eklentiler/_ana_butonlar.py` içerisindedir..",
        reply_markup=InlineKeyboardMarkup(data_butonlar)
    )

@Client.on_callback_query(filters.regex(pattern=r"^t.me/keyiflerolsun$"))
async def keyif_data(client:Client, callback_query:CallbackQuery):
    await callback_query.answer('t.me/keyiflerolsun a bastın kanka', show_alert=True)

@Client.on_callback_query(filters.regex(pattern=r"^t.me/KekikAkademi$"))
async def yksl_data(client:Client, callback_query:CallbackQuery):
    await callback_query.answer('t.me/KekikAkademi e bastın kanka', show_alert=True)