import os
import pymongo
from pymongo import MongoClient

#-------------------------------------------------------------------------------
# Replace these with your server details
#  MONGO_DB = os.environ['MONGODB_DATABASE']
MONGO_HOST = os.getenv('MONGODB_HOSTNAME', '127.0.0.1')
MONGO_PORT = os.getenv('MONGODB_PORT', '27017')
MONGO_USER = os.getenv('MONGODB_USERNAME', 'klaus')
MONGO_PASS = os.getenv('MONGODB_PASSWORD', 'klaus0505')

#  MONGO_HOST = "140.118.70.75"
#  MONGO_HOST = "127.0.0.1"
#  MONGO_PORT = "27017"
#  MONGO_USER = "root"
#  MONGO_PASS = "pc152"

#  uri = "mongodb://{}:{}@{}:{}/{}?authSource=admin".format(MONGO_USER, MONGO_PASS, MONGO_HOST, MONGO_PORT, MONGO_DB)
uri = "mongodb://{}:{}@{}:{}/".format(MONGO_USER, MONGO_PASS, MONGO_HOST, MONGO_PORT)
conn = MongoClient(uri, connect=False)
db = conn['sega']
#-------------------------------------------------------------------------------


data = [{"title": "アイドル雀士 スーチーパイ II", "time": "1996/4/26", "number": "9.2925"},
{"title": "スーパーリアル麻雀PV", "time": "1995/5/26","number": "8.7022"},
{"title": "野々村病院の人々", "time": "1996/4/26", "number": "8.6767"},
{"title": "ときめき麻雀グラフティ～年下の天使たち～", "time": "1996/5/1", "number": "8.4722"},
{"title": "アイドル雀士 スーチーパイ リミックス", "time": "1995/9/29", "number": "8.2962"},
{"title": "プレイボーイ カラオケ Vol.1", "time": "1996/8/9", "number": "8.2"},
{"title": "スーパーリアル麻雀PVI", "time": "1996/5/17", "number": "8.0765"},
{"title": "スーパーリアル麻雀グラフィティ", "time": "1995/11/24", "number": "8.027"},
{"title": "きゃんきゃんバニー・プルミエール", "time": "1996/4/5", "number": "7.4558"},
{"title": "アイドル麻雀 ファイナルロマンスR", "time": "1996/3/15", "number": "7.2654"},
{"title": "マイ・ベスト・フレンズ ～st.アンドリュー女学院編～", "time": "1996/3/22", "number": "7.1836"},
{"title": "バーチヤフォトスタジオ", "time": "1996/3/29", "number": "7.1666"},
{"title": "麻雀同級生Special", "time": "1996/3/29", "number": "7.1203"},
{"title": "ときめき麻雀パラダイス ～恋のてんぱいビート～", "time": "1995/10/20", "number": "6.9009"},
{"title": "アイドル麻雀 ファイナルロマンス2", "time": "1995/8/11", "number": "6.535"},
{"title": "ホーンテッドカジノ", "time": "1996/9/27", "number": "6.423"},
{"title": "天地無用！ 魎皇鬼ごくらくCD-ROM for SEGA SATURN", "time": "1995/9/29", "number": "6.1417"},
{"title": "THE野球拳スペシャル～今夜は12回戦～", "time": "1995/7/28", "number": "6.1311"},
{"title": "モータルコンバットII完全版", "time": "1996/3/29", "number": "5.7831"},
{"title": "麻雀天使エンジェルリップス", "time": "1996/3/29", "number": "5.6296"},
{"title": "麻雀ハイパーリアクションR", "time": "1996/3/8", "number": "5.2465"},
{"title": "GALJAN", "time": "1996/8/9", "number": "	4.7812"},
{"title": "麻雀四姉妹 若草物語", "time": "1996/9/27", "number": "3.2238"},
{"title": "アイドル麻雀ファイナルロマンスR プレミアムパッケージ", "time": "1996/5/31", "number": "*"},
{"title": "プレイボーイ カラオケ Vol.2", "time": "1996/8/9", "number": "*"}]

db.saturnGameList.insert_many(data)
