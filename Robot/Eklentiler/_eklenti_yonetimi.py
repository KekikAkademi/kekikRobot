# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Robot.Edevat.zenginLog import log_yolla, hata_log
from Robot import DESTEK_KOMUT

DESTEK_KOMUT.update({
    "eklenti" : {
        "aciklama"  : None,
        "kullanim"  : [
            None
            ],
        "ornekler"  : [
            ".eklentilist",
            ".eklentiver ping",
            ".eklential «Yanıtlanan Eklenti»",
            ".eklentisil !komut"
            ]
    }
})

from Robot.Edevat._pyrogram.pyro_yardimcilari import yanitlanan_mesaj
from Robot import SESSION_ADI, YETKILI
from Robot.Edevat.eklenti_listesi import eklentilerim
from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio, os

mesaj_baslangici = '`Hallediyorum..`'

@Client.on_message(filters.command(['eklentilist'], ['!','.','/']))
async def eklenti_list(client:Client, message:Message):
    # < Başlangıç
    await log_yolla(client, message)
    yanit_id  = await yanitlanan_mesaj(message)
    ilk_mesaj = await message.reply(mesaj_baslangici,
        reply_to_message_id      = yanit_id,
        disable_web_page_preview = True
    )
    #------------------------------------------------------------- Başlangıç >

    mesaj = "__Eklentilerim;__\n"
    mesaj += eklentilerim()

    try:
        await ilk_mesaj.edit(mesaj)
    except Exception as hata:
        await hata_log(hata, client, ilk_mesaj)

@Client.on_message(filters.command(['eklentiver'], ['!','.','/']))
async def eklenti_ver(client:Client, message:Message):
    # < Başlangıç
    await log_yolla(client, message)
    yanit_id  = await yanitlanan_mesaj(message)
    ilk_mesaj = await message.reply(mesaj_baslangici,
        reply_to_message_id      = yanit_id,
        disable_web_page_preview = True
    )
    #------------------------------------------------------------- Başlangıç >
    girilen_yazi = message.text

    if len(girilen_yazi.split()) == 1:
        await ilk_mesaj.edit("`DosyaAdı` **Girmelisin!**")
        return

    dosya = " ".join(girilen_yazi.split()[1:2])

    if f"{dosya}.py" in os.listdir("Robot/Eklentiler"):
        await ilk_mesaj.delete()

        await message.reply_document(
            document                = f"./Robot/Eklentiler/{dosya}.py",
            caption                 = f"__{SESSION_ADI}__ `{dosya}` __eklentisi..__",
            disable_notification    = True,
            reply_to_message_id     = yanit_id
            )

    else:
        await ilk_mesaj.edit('**Dosya Bulunamadı!**')

@Client.on_message(filters.command(['eklential'], ['!','.','/']))
async def eklenti_al(client:Client, message:Message):
    # < Başlangıç
    await log_yolla(client, message)
    yanit_id  = await yanitlanan_mesaj(message)

    if message.from_user.id not in YETKILI:
        await message.reply("⚠️ __admin değilmişsin kekkooo__", reply_to_message_id=yanit_id)
        return

    ilk_mesaj = await message.reply(mesaj_baslangici,
        reply_to_message_id      = yanit_id,
        disable_web_page_preview = True
    )
    #------------------------------------------------------------- Başlangıç >

    cevaplanan_mesaj = message.reply_to_message

    if len(message.command) == 1 and cevaplanan_mesaj.document:
        if cevaplanan_mesaj.document.file_name.split(".")[-1] != "py":
            await ilk_mesaj.edit("`Yalnızca python dosyası yükleyebilirsiniz..`")
            return
        eklenti_dizini = f"./Robot/Eklentiler/{cevaplanan_mesaj.document.file_name}"
        await ilk_mesaj.edit("`Eklenti Yükleniyor...`")

        if os.path.exists(eklenti_dizini):
            await ilk_mesaj.edit(f"`{cevaplanan_mesaj.document.file_name}` __eklentisi zaten mevcut!__")
            return

        try:
            await client.download_media(message=cevaplanan_mesaj, file_name=eklenti_dizini)
            await asyncio.sleep(2)
            await ilk_mesaj.edit(f"**Eklenti Yüklendi:** `{cevaplanan_mesaj.document.file_name}`")
            return

        except Exception as hata:
            await hata_log(hata, client, ilk_mesaj)
            return

    await ilk_mesaj.edit('__python betiği yanıtlamanız gerekmekte__')

@Client.on_message(filters.command(['eklentisil'], ['!','.','/']))
async def eklenti_sil(client:Client, message:Message):
    # < Başlangıç
    await log_yolla(client, message)
    yanit_id  = await yanitlanan_mesaj(message)

    if message.from_user.id not in YETKILI:
        await message.reply("⚠️ __admin değilmişsin kekkooo__", reply_to_message_id=yanit_id)
        return

    ilk_mesaj = await message.reply(mesaj_baslangici,
        reply_to_message_id      = yanit_id,
        disable_web_page_preview = True
    )
    #------------------------------------------------------------- Başlangıç >

    if len(message.command) == 2:
        eklenti_dizini = f"./Robot/Eklentiler/{message.command[1]}.py"

        if os.path.exists(eklenti_dizini):
            os.remove(eklenti_dizini)
            await asyncio.sleep(2)
            await ilk_mesaj.edit(f"**Eklenti Silindi:** `{message.command[1]}`")
            return

        await ilk_mesaj.edit("`Böyle bir eklenti yok`")
        return

    await ilk_mesaj.edit("`Geçerli bir eklenti adı girin!`")