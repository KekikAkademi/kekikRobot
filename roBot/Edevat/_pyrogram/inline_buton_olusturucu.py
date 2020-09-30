# https://github.com/MuhendisKoyu/HangisiniOgrenmeli

from pyrogram.types import InlineKeyboardButton

def dilimleyici(buton_listesi:list, adet:int=2) -> list:
    return [buton_listesi[i : i + adet] for i in range(0, len(buton_listesi), adet)]

def butonOlustur(butonlar:dict, adet:int, link:str=False, data:str=False, geri:str=None, ana_sayfa:str=None) -> list:
    """
    Bu Fonksiyon Sayesinde Buton Oluşturmak Çok Kolay
    
        butonOlustur(butonlar=dict, adet=3, link=True)
        butonOlustur(butonlar=dict, adet=3, link=True, geri='geri_don')
        butonOlustur(butonlar=dict, adet=3, data=True, ana_Sayfa='ana_sayfa')
    """
    if link:
        butonlar: list = [InlineKeyboardButton(text=key, url=value) for key, value in butonlar.items()]
        butonlar = dilimleyici(butonlar, adet)

    if data:
        butonlar: list = [InlineKeyboardButton(text=key, callback_data=value) for key, value in butonlar.items()]
        butonlar = dilimleyici(butonlar, adet)

    if ana_sayfa:
        geri_butonu: InlineKeyboardButton = InlineKeyboardButton(text="🏘 Ana Sayfa", callback_data=ana_sayfa)
        butonlar.append([geri_butonu])

    if geri:
        geri_butonu: InlineKeyboardButton = InlineKeyboardButton(text="🔙 Geri", callback_data=geri)
        butonlar.append([geri_butonu])

    return butonlar