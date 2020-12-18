# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import os, json

def dict2json(sozluk:dict, liste_key:str, dosya_adi:str) -> None:
    if os.path.isfile(dosya_adi):
        with open(dosya_adi) as gelen_json:
            gelen_veri = json.load(gelen_json)

        gelen_veri.append(sozluk)
        gelen_essiz = [dict(sozluk) for sozluk in {tuple(liste_ici.items()) for liste_ici in gelen_veri}]
        gelen_a_z   = sorted(gelen_essiz, key=lambda sozluk: sozluk[liste_key])

        with open(dosya_adi, mode='w') as f:
            f.write(json.dumps(gelen_a_z, indent=2, ensure_ascii=False, sort_keys=False))

    else:
        with open(dosya_adi, mode='w') as f:
            liste = [sozluk]
            essiz = [dict(sozluk) for sozluk in {tuple(liste_ici.items()) for liste_ici in liste}]
            a_z   = sorted(essiz, key=lambda sozluk: sozluk[liste_key])
            f.write(json.dumps(a_z, indent=2, ensure_ascii=False, sort_keys=False))