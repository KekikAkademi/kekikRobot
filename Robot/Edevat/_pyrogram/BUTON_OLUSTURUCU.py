# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.
    # https://github.com/MuhendisKoyu/HangisiniOgrenmeli

from pyrogram.types import InlineKeyboardButton, ReplyKeyboardMarkup

def dilimleyici(buton_listesi:list, adet:int=2) -> list:
    return [buton_listesi[i : i + adet] for i in range(0, len(buton_listesi), adet)]

def buton_ver(liste:list, adet:int) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(dilimleyici(liste, adet), resize_keyboard = True)

def buton_olustur(butonlar:dict, adet:int, link:bool=False, data:bool=False, geri:str=None, ana_sayfa:str=None) -> list:
    """
    Bu Fonksiyon Sayesinde Buton Oluşturmak Çok Kolay

        butonOlustur(butonlar=dict, adet=3, link=True)
        butonOlustur(butonlar=dict, adet=3, link=True, geri='geri_don')
        butonOlustur(butonlar=dict, adet=3, data=True, ana_Sayfa='ana_sayfa')
    """
    gidecek_buton = []
    if link:
        gidecek_buton: list = [InlineKeyboardButton(text=key, url=value) for key, value in butonlar.items()]
        gidecek_buton = dilimleyici(gidecek_buton, adet)

    if data:
        gidecek_buton: list = [InlineKeyboardButton(text=key, callback_data=value) for key, value in butonlar.items()]
        gidecek_buton = dilimleyici(gidecek_buton, adet)

    if ana_sayfa:
        geri_butonu: InlineKeyboardButton = InlineKeyboardButton(text="🏘 Ana Sayfa", callback_data=ana_sayfa)
        gidecek_buton.append([geri_butonu])

    if geri:
        geri_butonu: InlineKeyboardButton = InlineKeyboardButton(text="🔙 Geri", callback_data=geri)
        gidecek_buton.append([geri_butonu])

    return gidecek_buton