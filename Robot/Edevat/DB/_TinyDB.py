# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.
 
from tinydb import TinyDB, Query
from tinydb.operations import delete
from tinydb.queries import QueryLike
from Robot import SESSION_ADI

class kekikRobotDB:
    def __init__(self):
        TinyDB.default_table_name = self.__class__.__name__
        self.db    = TinyDB(f"@{SESSION_ADI}_DB.json", ensure_ascii=False, indent=2, sort_keys=False)
        self.sorgu = Query()

    def ara(self, sorgu:QueryLike):
        arama = self.db.search(sorgu)
        say   = len(arama)
        if say == 1:
            return arama[0]
        elif say > 1:
            cursor = arama
            return {
                bak['uye_id'] : {
                    "uye_nick"   : bak['uye_nick'],
                    "uye_adi"    : bak['uye_adi']
                }
                for bak in cursor
            }
        else:
            return None

    def ekle(self, uye_id, uye_nick, uye_adi):
        if not self.ara(self.sorgu.uye_id == uye_id):
            return self.db.insert({
                "uye_id"     : uye_id,
                "uye_nick"   : uye_nick,
                "uye_adi"    : uye_adi,
            })
        else:
            return None

    def sil(self, uye_id):
        if not self.ara(self.sorgu.uye_id == uye_id):
            return None

        # self.db.update(delete('uye_id'), self.sorgu.uye_id == uye_id)
        self.db.remove(self.sorgu.uye_id == uye_id)
        return True

    @property
    def kullanicilar(self):
        return self.ara(self.sorgu.uye_id.exists())