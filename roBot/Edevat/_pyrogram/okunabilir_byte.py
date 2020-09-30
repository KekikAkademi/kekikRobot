# https://github.com/Skuzzy_xD/TelePyroBot

def okunabilirByte(boyut: int) -> str:
    """ baytları okunabilir biçime dönüştürür """
    # https://stackoverflow.com/a/49361727/4723940
    # 2**10 = 1024
    if not boyut:
        return ""
    binyirmidort = 2 ** 10
    say = 0
    cikti_sozluk = {0: " ", 1: "K", 2: "M", 3: "G", 4: "T"}
    while boyut > binyirmidort:
        boyut /= binyirmidort
        say += 1
    return str(round(boyut, 2)) + " " + cikti_sozluk[say] + "B"