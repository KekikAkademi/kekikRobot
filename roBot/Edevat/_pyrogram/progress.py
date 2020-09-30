# https://github.com/Skuzzy_xD/TelePyroBot

from roBot.Edevat._pyrogram.okunabilir_byte import okunabilirByte
from roBot.Edevat._pyrogram.zaman_donustur import zamanDonustur
import math, time

async def pyroProgress(gecerli, toplam, olay_turu, mesaj, baslangic):
    """ Telegram Yükleme / İndirme durumu için genel ilerleme ekranı """
    simdi = time.time()
    degisim = simdi - baslangic
    if round(degisim % 10.00) == 0 or gecerli == toplam:
        # if round(gecerli / toplam * 100, 0) % 5 == 0:
        yuzde = gecerli * 100 / toplam
        hiz = gecerli / degisim
        gecen_zaman = round(degisim)
        tamamlanma_zamani = round((toplam - gecerli) / hiz)
        tahmini_toplam_sure = tamamlanma_zamani

        print(f"""
        simdi       : {zamanDonustur(simdi)}
        baslangic   : {zamanDonustur(baslangic)}
        degisim     : {zamanDonustur(degisim)}
        yuzde       : {round(yuzde, 2)}
        hiz         : {okunabilirByte(hiz)}
        gecen zamn  : {zamanDonustur(gecen_zaman)}
        tamamlanma  : {zamanDonustur(tamamlanma_zamani)}
        tahmini     : {zamanDonustur(tahmini_toplam_sure)}
        """)

        gecen_zaman = zamanDonustur(gecen_zaman)
        tahmini_toplam_sure = zamanDonustur(tahmini_toplam_sure)

        progress = "**[{0}{1}]**\n**Süreç**: `%{2}`\n".format(
            "".join(["●" for i in range(math.floor(yuzde / 5))]),       # 🟥 █ ●
            "".join(["○" for i in range(20 - math.floor(yuzde / 5))]),  # ⬜ ░ ○
            round(yuzde, 2),
        )

        toparla = progress
        toparla += f"**Başarılı:** **{okunabilirByte(toplam)}**__'dan__ `{okunabilirByte(gecerli)}`\n"
        toparla += f"**Hız:** `{okunabilirByte(hiz)}/s`\n"
        toparla += f"**Tahmini:** __{tahmini_toplam_sure if tahmini_toplam_sure else 'Bitti de son bi kaç ayar yapıyorum..'}__\n"
        try:
            await mesaj.edit(f"{olay_turu}\n {toparla}")
        except:
            pass