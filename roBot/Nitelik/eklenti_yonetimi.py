# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from roBot.Nitelik import logYolla, DESTEK_KOMUT
from pathlib import Path

DESTEK_KOMUT.update({
    Path(__file__).stem : {
        "aciklama"  : None,
        "kullanim"  : [
            None
            ],
        "ornekler"  : [
            ".eklentilist",
            ".eklentiver ping",
            ".eklential «Yanıtlanan Eklenti»",
            ".eklentisil yt"
            ]
    }
})

from roBot.Edevat._from_nana.pyro_yardimcilari import ReplyCheck
from pyrogram import Client, filters
import asyncio, os, json

bilgiler = json.load(open("bilgiler.json"))

@Client.on_message(filters.command(['eklentilist'], ['!','.','/']))
async def eklenti_list(client, message):
    # < Başlangıç
    await logYolla(client, message)
    ilk_mesaj = await message.reply("__Bekleyin..__",
        reply_to_message_id         = ReplyCheck(message),
        disable_web_page_preview    = True,
        parse_mode                  = "Markdown"
    )
    #------------------------------------------------------------- Başlangıç >

    mesaj = "__Eklentilerim;__\n"

    for dosya in os.listdir("./roBot/Eklentiler/"):
        if not dosya.endswith(".py") or dosya.endswith("__.py"):
            continue
        mesaj += f"📂 `{dosya.replace('.py','')}`\n"
    
    try:
        await ilk_mesaj.edit(mesaj)
    except Exception as hata:
        await ilk_mesaj.edit(f"**Uuppss:**\n\n`{hata}`")

@Client.on_message(filters.command(['eklentiver'], ['!','.','/']))
async def eklenti_ver(client, message):
    # < Başlangıç
    await logYolla(client, message)
    yanitlanacak_mesaj = ReplyCheck(message)
    ilk_mesaj = await message.reply("__Bekleyin..__",
        reply_to_message_id         = yanitlanacak_mesaj,
        disable_web_page_preview    = True,
        parse_mode                  = "Markdown"
    )
    #------------------------------------------------------------- Başlangıç >
    
    girilen_yazi = message.text                                 # komut ile birlikle mesajı tut

    if len(girilen_yazi.split()) == 1:                          # eğer sadece komut varsa
        await ilk_mesaj.edit("`DosyaAdı` **Girmelisin!**")      # uyarı ver
        return                                                  # geri dön

    dosya = " ".join(girilen_yazi.split()[1:2])                 # dosyayı komuttan ayır (birinci kelime)

    if f"{dosya}.py" in os.listdir("roBot/Eklentiler"):
        await ilk_mesaj.delete()

        await message.reply_document(
            document                = f"./roBot/Eklentiler/{dosya}.py",
            caption                 = f"__kekikUserBot__ `{dosya}` __eklentisi..__",
            disable_notification    = True,
            reply_to_message_id     = yanitlanacak_mesaj
            )

    else:
        await ilk_mesaj.edit('**Dosya Bulunamadı!**')

@Client.on_message(filters.command(['eklential'], ['!','.','/']))
async def eklenti_al(client, message):
    # < Başlangıç
    await logYolla(client, message)
    ilk_mesaj = await message.reply("__Bekleyin..__",
        reply_to_message_id         = ReplyCheck(message),
        disable_web_page_preview    = True,
        parse_mode                  = "Markdown"
    )

    cevaplanan_mesaj = message.reply_to_message
    #------------------------------------------------------------- Başlangıç >
    
    if message.from_user.id not in bilgiler['yetkili']:
        await ilk_mesaj.edit("__admin değilmişsin kekkooo__")
        return
    
    if len(message.command) == 1 and cevaplanan_mesaj.document:
        if cevaplanan_mesaj.document.file_name.split(".")[-1] != "py":
            await ilk_mesaj.edit("`Yalnızca python dosyası yükleyebilirsiniz..`")
            return
        eklenti_dizini = f"./roBot/Eklentiler/{cevaplanan_mesaj.document.file_name}"
        await ilk_mesaj.edit("`Eklenti Yükleniyor...`")
        
        if os.path.exists(eklenti_dizini):
            await ilk_mesaj.edit(f"`{cevaplanan_mesaj.document.file_name}` __eklentisi zaten mevcut!__")
            return
        
        try:
            eklenti_indir = await client.download_media(message=cevaplanan_mesaj, file_name=eklenti_dizini)
            await asyncio.sleep(2)
            await ilk_mesaj.edit(f"**Eklenti Yüklendi:** `{cevaplanan_mesaj.document.file_name}`")
            return

        except Exception as hata:
            await ilk_mesaj.edit(f"**Uuppss:**\n\n`{hata}`")
    
    await ilk_mesaj.edit('__python betiği yanıtlamanız gerekmekte__')
    return

@Client.on_message(filters.command(['eklentisil'], ['!','.','/']))
async def eklenti_sil(client, message):
    # < Başlangıç
    await logYolla(client, message)
    ilk_mesaj = await message.reply("__Bekleyin..__",
        reply_to_message_id         = ReplyCheck(message),
        disable_web_page_preview    = True,
        parse_mode                  = "Markdown"
    )
    #------------------------------------------------------------- Başlangıç >

    if message.from_user.id not in bilgiler['yetkili']:
        await ilk_mesaj.edit("__admin değilmişsin kekkooo__")
        return

    if len(message.command) == 2:
        eklenti_dizini = f"./roBot/Eklentiler/{message.command[1]}.py"
        
        if os.path.exists(eklenti_dizini):
            os.remove(eklenti_dizini)
            await asyncio.sleep(2)
            await ilk_mesaj.edit(f"**Eklenti Silindi:** `{message.command[1]}`")
            return
        
        await ilk_mesaj.edit("`Böyle bir eklenti yok`")
        return
    
    await ilk_mesaj.edit("`Geçerli bir eklenti adı girin!`")
    return