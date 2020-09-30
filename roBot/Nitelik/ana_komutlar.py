# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from roBot.Nitelik import logYolla
from roBot.Edevat._from_nana.pyro_yardimcilari import ReplyCheck
from roBot.Edevat._from_nana.deldog import deldog

from pyrogram import Client, filters
from time import time
from os import listdir
import asyncio, json

bilgiler = json.load(open("bilgiler.json"))

# Ana Komutlar
@Client.on_message(filters.command(['yardim'], ['!','.','/']))
async def yardim_mesaji(client, message):
    """ .yardim komutu için """
    # < Başlangıç
    await logYolla(client, message)
    ilk_mesaj = await message.reply("__Bekleyin..__",
        reply_to_message_id         = ReplyCheck(message),
        disable_web_page_preview    = True,
        parse_mode                  = "Markdown"
    )
    #------------------------------------------------------------- Başlangıç >
    
    basla = time()
    await ilk_mesaj.edit("__Aranıyor...__")

    mesaj = f"""Merhaba, [{message.from_user.first_name}](tg://user?id={message.from_user.id})!\n
Ben @keyiflerolsun tarafından, @KekikAkademi'de yaratıldım.\n
Kaynak kodlarım [Burada](https://github.com/KekikAkademi/Client)
Kullanabileceğim komutlar ise eklentilerimde gizli..\n\n"""

    mesaj += """__Eklentilerimi görebilmek için__ `.eklentilist` __komutunu kullanabilirsin..__
    
`.destek` «__eklenti__» **komutuyla da eklenti hakkında bilgi alabilirsin..**
"""

    bitir = time()
    sure = bitir - basla
    mesaj += f"\n**Tepki Süresi :** `{str(sure)[:4]} sn`"

    try:
        await ilk_mesaj.edit(mesaj, disable_web_page_preview=True)
    except Exception as hata:
        await ilk_mesaj.edit(f"**Uuppss:**\n\n`{hata}`")


DESTEK_KOMUT = {}

@Client.on_message(filters.command(['destek'], ['!','.','/']))
async def destek(client, message):
    """ .destek komutu için """
    # < Başlangıç
    await logYolla(client, message)
    ilk_mesaj = await message.reply("__Bekleyin..__",
        reply_to_message_id         = ReplyCheck(message),
        disable_web_page_preview    = True,
        parse_mode                  = "Markdown"
    )
    #------------------------------------------------------------- Başlangıç >

    girilen_yazi = message.text.split()                             # komut ile birlikle mesajı tut

    if len(girilen_yazi) == 1:                                      # eğer sadece komut varsa
        mesaj = "`DosyaAdı` **Girmelisin!**\n\n"                    # uyarı ver

        mesaj += "__Destek alınabilecek Eklentilerim;__\n"

        for dosya in listdir("./roBot/Eklentiler/"):
            if not dosya.endswith(".py") or dosya.endswith("__.py"):
                continue
            mesaj += f"📂 `{dosya.replace('.py','')}`\n"
        await ilk_mesaj.edit(mesaj)
        return

    try:
        if girilen_yazi[1] == 'eklenti':
            destek_json = DESTEK_KOMUT['eklenti_yonetimi']
            mesaj = f"**{bilgiler['session']}** __Eklenti Yönetim Sistemi__\n"
        else:
            eklenti_dizini = f"./roBot/Eklentiler/{girilen_yazi[1]}.py"
            destek_json = DESTEK_KOMUT[girilen_yazi[1]]
            mesaj = f"\t📝\t `{girilen_yazi[1]}` <u>**Eklentisi;**</u>\n"

        if destek_json['aciklama']:
            mesaj += f"__{destek_json['aciklama']}__\n"

        if destek_json['kullanim'][0]:
            mesaj += "\n\t✒️ <u>**Kullanım;**</u>\n"
            for destek_parametre in destek_json['kullanim']:
                mesaj += f"\t«<i>{destek_parametre}</i>»\n"

        if destek_json['ornekler'][0]:
            mesaj += f"\n\t✏️ <u>**Örneğin;**</u>\n"
            for destek_ornek in destek_json['ornekler']:
                mesaj += f"```{destek_ornek}```\n"

    except KeyError:
        mesaj = f"`{girilen_yazi[1]}`\n\t**Adında bir eklenti bulunamadı..**"

        mesaj += "\n\n__Destek alınabilecek Eklentilerim;__\n"

        for dosya in listdir("./roBot/Eklentiler/"):
            if not dosya.endswith(".py") or dosya.endswith("__.py"):
                continue
            mesaj += f"📂 `{dosya.replace('.py','')}`\n"

    await ilk_mesaj.edit(mesaj)

@Client.on_message(filters.command(['logsalla'], ['!','.','/']))
async def logsalla(client, message):
    """ .logsalla komutu için """
    # < Başlangıç
    await logYolla(client, message)
    yanitlanacak_mesaj = ReplyCheck(message)
    ilk_mesaj = await message.reply("__Bekleyin..__",
        reply_to_message_id         = yanitlanacak_mesaj,
        disable_web_page_preview    = True,
        parse_mode                  = "Markdown"
    )
    #------------------------------------------------------------- Başlangıç >

    if message.from_user.id not in bilgiler['yetkili']:
        await message.reply("__admin değilmişsin kekkooo__", reply_to_message_id=yanitlanacak_mesaj)
        return
    
    f = open(f"@{bilgiler['session']}.log", "r")
    raw_log = await deldog(message, f.read())

    await message.reply(
        f"**Log istersin de vermez miyim..**\n\n__[@{bilgiler['session']} Logları]({raw_log})__",
        disable_web_page_preview    = True,
        reply_to_message_id         = yanitlanacak_mesaj
    )
   
    # await message.reply_document(
    #     document                = f"@{bilgiler['session']}.log",
    #     caption                 = f"@{message.from_user.username} __için gönderdim..__",
    #     disable_notification    = True,
    #     reply_to_message_id     = yanitlanacak_mesaj
    # )