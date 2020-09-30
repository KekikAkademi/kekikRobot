# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Ana Butonlar
start_mesajı = "Hoş Geldin!\n/yardim alabilirsin"

start_butonu = [[InlineKeyboardButton("📚 Yardım", callback_data="yardim"), InlineKeyboardButton("ℹ️ Hakkımda", url="https://t.me/KekikAkademi")]]
start_butonu += [[InlineKeyboardButton("💸 Bağışta Bulun", url="https://t.me/KekikAkademi/1190")]]

yardim_butonu = [
    [
        InlineKeyboardButton("👤 Beni Gruba Ekle", url="https://t.me/Client?startgroup=ch"),
        InlineKeyboardButton("👷 Kodlarıma Ulaş", url="https://github.com/KekikAkademi")
    ],
    [
        InlineKeyboardButton("🔙 Geri", callback_data="geri_don")
    ]
]

@Client.on_message(filters.command(['start'], ['!','.','/']))
async def start_buton(client, message):
    """ .start komutu için """
    
    # Hoş Geldin Mesajı
    await message.reply(start_mesajı, reply_markup=InlineKeyboardMarkup(start_butonu))

@Client.on_callback_query(filters.regex(pattern=r"^geri_don$"))
async def geri_don_bilgisi(client, callback_query):
    """ geri Bilgisi için """

    await callback_query.edit_message_text(start_mesajı, reply_markup=InlineKeyboardMarkup(start_butonu))
    await callback_query.answer('Afferin !\nGeri dönmeyi başaran ilk kişi oldun..', show_alert=True)

@Client.on_callback_query(filters.regex(pattern=r"^yardim$"))
async def yardim_bilgisi(client, callback_query):
    """ yardim Bilgisi için """

    await callback_query.edit_message_text(
        "__Ana Komutlarım Şunlar:__\n\n`.yardim`\n`.destek`\n`.logsalla`\n\n**Diğer komutlarım için /eklentilist'e bakabilirsin..**",
        reply_markup=InlineKeyboardMarkup(yardim_butonu)
    )

@Client.on_callback_query(filters.regex(pattern=r"^ana_sayfa$"))
async def ana_sayfa(client, callback_query):
    """ ana_sayfa Bilgisi için """

    await callback_query.edit_message_text(
        start_mesajı, reply_markup=InlineKeyboardMarkup(start_butonu)
    )