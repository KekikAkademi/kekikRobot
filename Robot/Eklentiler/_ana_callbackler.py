# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery
from pyrogram.types import InlineKeyboardMarkup

from Robot import SESSION_ADI
from Robot.Edevat._pyrogram.BUTON_OLUSTURUCU import buton_olustur

@Client.on_callback_query(filters.regex(pattern=r"^📚 Yardım$"))
async def yardim_callback(client:Client, callback_query:CallbackQuery):
    await callback_query.edit_message_text(
        "__Ana Komutlarım Şunlar:__\n\n`.yardim`\n`.destek`\n`.logsalla`\n\n**Diğer komutlarım için /eklentilist'e bakabilirsin..**",
        reply_markup = InlineKeyboardMarkup(buton_olustur({
                "👤 Beni Gruba Ekle" : f"https://t.me/{SESSION_ADI}?startgroup=ch",
                "👷 Kodlarıma Ulaş"  : "https://github.com/KekikAkademi/kekikRobot"
            }, adet=2, link=True)
        )
    )

@Client.on_callback_query(filters.regex(pattern=r"^🏘 Ana Sayfa$"))
async def ana_sayfa_callback(client:Client, callback_query:CallbackQuery):
    await callback_query.edit_message_text(
        "Hoş Geldin!\n/yardim alabilirsin",
        reply_markup = InlineKeyboardMarkup(buton_olustur({
                "📚 Yardım" : "📚 Yardım"
            }, adet=1, data=True)
        )
    )