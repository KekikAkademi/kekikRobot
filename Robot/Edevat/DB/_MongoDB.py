# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.
 
import pymongo
from Robot import MONGO_DB, SESSION_ADI

class kekikRobotDB:
    def __init__(self):
        client          = pymongo.MongoClient(MONGO_DB)
        db              = client['Telegram']
        self.collection = db[SESSION_ADI]

    def ara(self, sorgu:dict):
        say = self.collection.count_documents(sorgu)
        if say == 1:
            return self.collection.find_one(sorgu, {'_id': 0})
        elif say > 1:
            cursor = self.collection.find(sorgu, {'_id': 0})
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
        if not self.ara({'uye_id': {'$in': [str(uye_id), int(uye_id)]}}):
            return self.collection.insert_one({
                "uye_id"     : uye_id,
                "uye_nick"   : uye_nick,
                "uye_adi"    : uye_adi,
            })
        else:
            return None

    def sil(self, uye_id):
        if not self.ara({'uye_id': {'$in': [str(uye_id), int(uye_id)]}}):
            return None

        self.collection.delete_one({'uye_id': {'$in': [str(uye_id), int(uye_id)]}})
        return True

    @staticmethod
    def kullanicilar(self):
        return list(self.ara({'uye_id': {'$gt': 0}}).keys())