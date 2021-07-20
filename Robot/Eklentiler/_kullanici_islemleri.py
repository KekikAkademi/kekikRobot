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
            ".duyuru «Yanıtlanan Mesaj»",
            ]
    }
})


from pyrogram import Client, filters
from pyrogram.types import Message
from Robot import YETKILI

from Robot import kekikRobotDB

@Client.on_message(filters.command(['kull_say'], ['!','.','/']))
async def kull_say(client:Client, message:Message):
    # < Başlangıç
    await log_yolla(client, message)

    if message.from_user.id not in YETKILI:
        return await message.reply("⚠️ __admin değilmişsin kekkooo__")

    ilk_mesaj = await message.reply("⌛️ `Hallediyorum..`",
        quote                    = True,
        disable_web_page_preview = True
    )
    #------------------------------------------------------------- Başlangıç >

    db = kekikRobotDB()
    KULLANICILAR = lambda : db.kullanici_idleri

    await ilk_mesaj.edit(f"ℹ️ `{len(KULLANICILAR())}` __Adet Kullanıcıya Sahipsin..__")

@Client.on_message(filters.command(['duyuru'], ['!','.','/']))
async def duyuru(client:Client, message:Message):
    # < Başlangıç
    await log_yolla(client, message)

    if message.from_user.id not in YETKILI:
        return await message.reply("⚠️ __admin değilmişsin kekkooo__")

    ilk_mesaj = await message.reply("⌛️ `Hallediyorum..`",
        quote                    = True,
        disable_web_page_preview = True
    )
    #------------------------------------------------------------- Başlangıç >

    db = kekikRobotDB()
    KULLANICILAR = lambda : db.kullanici_idleri

    if not KULLANICILAR():
        await ilk_mesaj.edit("ℹ️ __Start vermiş kimse yok kanka..__")
        return

    if not message.reply_to_message:
        await ilk_mesaj.edit("⚠️ __Duyurmak için mesaj yanıtlayın..__")
        return

    basarili = 0
    hatalar  = []
    mesaj_giden_kisiler = []
    for kullanici_id in KULLANICILAR():
        try:
            await client.copy_message(
                chat_id      = kullanici_id,
                from_chat_id = message.reply_to_message.chat.id,
                message_id   = message.reply_to_message.message_id
            )
            mesaj_giden_kisiler.append(kullanici_id)
            basarili += 1
        except Exception as hata:
            hatalar.append(type(hata).__name__)
            db.sil(kullanici_id)


    mesaj = f"⁉️ `{len(hatalar)}` __Adet Kişiye Mesaj Atamadım ve DB'den Sildim..__\n\n" if hatalar else ""
    mesaj += f"📜 `{basarili}` __Adet Kullanıcıya Mesaj Attım..__"

    await ilk_mesaj.edit(mesaj)