# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Robot.Edevat.zenginLog import log_yolla, hata_log
from Robot import DESTEK_KOMUT

DESTEK_KOMUT.update({
    "kull"          : {
        "aciklama"  : "Çeşitli Kullanıcı İşlemlerini Gerçekleştirebilirsiniz..",
        "kullanim"  : [
            None
            ],
        "ornekler"  : [
            ".kull_say",
            ".kull_ver",
            ".kull_al «Yanıtlanan Kullanıcı jSon»",
            ".duyuru «Yanıtlanan Mesaj»",
            ]
    }
})


from pyrogram import Client, filters
from pyrogram.types import Message
from Robot.Edevat._pyrogram.pyro_yardimcilari import yanitlanan_mesaj
from Robot import SESSION_ADI, YETKILI
import os, json

kullanicilar = f"{SESSION_ADI}_KULLANICILAR.json"

if not os.path.exists(kullanicilar):
    with open(kullanicilar, 'w+') as olustur:
        olustur.write('[]')

KULLANICILAR = lambda : json.load(open(kullanicilar, 'r'))

@Client.on_message(filters.command(['kull_say'], ['!','.','/']))
async def kull_say(client:Client, message:Message):
    # < Başlangıç
    await log_yolla(client, message)
    yanit_id  = await yanitlanan_mesaj(message)

    if message.chat.type != "private":
        return

    if str(message.from_user.id) not in YETKILI:
        await message.reply("__admin değilmişsin kekkooo__")
        return

    ilk_mesaj = await message.reply("`Hallediyorum..`",
        reply_to_message_id      = yanit_id,
        disable_web_page_preview = True
    )
    #------------------------------------------------------------- Başlangıç >

    await ilk_mesaj.edit(f"`{len(KULLANICILAR())}` __Adet Kullanıcıya Sahipsin..__")

@Client.on_message(filters.command(['kull_ver'], ['!','.','/']))
async def kull_ver(client:Client, message:Message):
    # < Başlangıç
    await log_yolla(client, message)
    yanit_id  = await yanitlanan_mesaj(message)

    if message.chat.type != "private":
        return

    if str(message.from_user.id) not in YETKILI:
        await message.reply("__admin değilmişsin kekkooo__")
        return

    ilk_mesaj = await message.reply("`Hallediyorum..`",
        reply_to_message_id      = yanit_id,
        disable_web_page_preview = True
    )
    #------------------------------------------------------------- Başlangıç >

    await ilk_mesaj.delete()
    await message.reply_document(document = kullanicilar)

@Client.on_message(filters.command(['kull_al'], ['!','.','/']))
async def kull_al(client:Client, message:Message):
    # < Başlangıç
    await log_yolla(client, message)
    yanit_id  = await yanitlanan_mesaj(message)

    if message.chat.type != "private":
        return

    if str(message.from_user.id) not in YETKILI:
        await message.reply("__admin değilmişsin kekkooo__")
        return

    ilk_mesaj = await message.reply("`Hallediyorum..`",
        reply_to_message_id      = yanit_id,
        disable_web_page_preview = True
    )
    #------------------------------------------------------------- Başlangıç >

    if (message.reply_to_message) and (message.reply_to_message.document) and (message.reply_to_message.document.file_name == kullanicilar):
        bakalim = await client.download_media(message=message.reply_to_message, file_name=kullanicilar)
        with open(kullanicilar, 'w+') as dosya:
            dosya.write(json.dumps(json.load(open(bakalim)), sort_keys=False, indent=2, ensure_ascii=False))

        await ilk_mesaj.edit("**Yeni liste kaydedildi..**")
        os.remove(bakalim)
    else:
        await ilk_mesaj.edit("__jajaja güldük..__")

@Client.on_message(filters.command(['duyuru'], ['!','.','/']))
async def duyuru(client:Client, message:Message):
    # < Başlangıç
    await log_yolla(client, message)
    yanit_id  = await yanitlanan_mesaj(message)

    if message.chat.type != "private":
        return

    if str(message.from_user.id) not in YETKILI:
        await message.reply("__admin değilmişsin kekkooo__")
        return

    ilk_mesaj = await message.reply("`Hallediyorum..`",
        reply_to_message_id      = yanit_id,
        disable_web_page_preview = True
    )
    #------------------------------------------------------------- Başlangıç >

    if not KULLANICILAR():
        await ilk_mesaj.edit("__Start vermiş kimse yok kanka..__")
        return

    if not message.reply_to_message:
        await ilk_mesaj.edit(f"__Duyurmak için mesaj yanıtlayın..__")
        return

    basarili = 0
    hatalar  = []
    for kullanici in KULLANICILAR():
        try:
            await client.copy_message(
                chat_id      = kullanici['kullanici_id'],
                from_chat_id = message.reply_to_message.chat.id,
                message_id   = message.reply_to_message.message_id
            )
            basarili += 1
        except Exception as hata:
            hatalar.append(type(hata).__name__)

    mesaj = f"`{basarili}` __Adet Kullanıcıya Mesaj Attım..__"
    mesaj += f"\n\n**Hatalar :** \n\n```{hatalar}```" if hatalar else ""

    await ilk_mesaj.edit(mesaj)
