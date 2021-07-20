# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from os import listdir

def eklentilerim() -> str:
    return "".join(
        f"📂 `{dosya.replace('.py','')}`\n"
            for dosya in listdir("./Robot/Eklentiler/")
                if dosya.endswith(".py") and not dosya.startswith("_")
    )