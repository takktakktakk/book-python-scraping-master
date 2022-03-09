import urllib.request as req
import datetime
import json

# web APIにアクセス
API = "https://api.aoikujira.com/kawase/get.php?code=USD&format=json"
with req.urlopen(API) as res:
    json_str = res.read().decode('utf-8')
    data = json.loads(json_str)
    print("1USD: {jpy}".format(jpy = data["JPY"]) + "円")

# 保存ファイル名を決定
t = datetime.datetime.now()
fname = "./ch2/" + t.strftime('%Y-%m-%d_%H:%M:%S') + ".json"

with open(fname, "w", encoding="utf-8") as f:
    f.write(json_str)
