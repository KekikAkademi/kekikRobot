# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from konsolTaban._evrensel import *
from konsolTaban._degiskenler.banner import *

#----------------------------------------------------#
def bildirim():
    if platform.machine() == "aarch64":
        return
    elif kullanici_adi == "gitpod":
        pass
    elif bellenim_surumu.split('-')[-1] == 'aws':
        pass
    elif isletim_sistemi == "Windows" and bellenim_surumu >= "10":
        try:
            from win10toast import ToastNotifier
        except:
            os.system('pip install win10toast')
            from win10toast import ToastNotifier

        bildirim = ToastNotifier()
        bildirim.show_toast(f"{pencere_basligi}", f"{bildirim_metni}",
            icon_path=None, duration=10, threaded=True
            )
    elif isletim_sistemi == "Linux":
        try:
            import notify2
        except:
            os.system('pip install notify2')
            import notify2

        notify2.init(pencere_basligi)
        bildirim = notify2.Notification(f"{pencere_basligi}", f"{bildirim_metni}", "notification-message-im")
        bildirim.show()
bildirim()
#----------------------------------------------------#