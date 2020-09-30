# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from konsolTaban._renkler import yesil
from konsolTaban._evrensel import ust_bilgi
from konsolTaban._degiskenler import logo

from roBot import kekikRobot, baslangic, tum_eklentiler
from roBot.Edevat import onemli, bilgi

#-------------------------------#
print(f"{yesil}{logo}")         # yeşil renk koduyla logomuzu yazdırdık
print(ust_bilgi)                # Üst Bilgimizi yazdırdık
baslangic()                     # Bot'u Aç Kapa - Banner
#-------------------------------#

eklentiler = ""
j = 1
for i in tum_eklentiler:
    if j == 3:
        eklentiler += "| {:<18} |\n".format(i) if len(tum_eklentiler) != 3 else "| {:<18} |".format(i)
        j = 0
    else:
        eklentiler += "| {:<18}".format(i)
    j += 1

onemli("+===============================================================+")
onemli("|                       Eklentilerim                            |")
onemli("+===============+===============+===============+===============+")
bilgi(f"{eklentiler}")
onemli("+===============+===============+===============+===============+\n")

if __name__ == "__main__":
    kekikRobot.run()