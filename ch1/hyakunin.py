#!/usr/bin/env python3

# ライブラリの取り込み --- (※1)
import urllib.request as req
import urllib.parse as parse

# コマンドライン引数を得る --- (※2)
keyword = input("百人一首のキーワードを入力してください：")

# パラメータをURLエンコードする --- (※3)
API = "https://api.aoikujira.com/hyakunin/get.php"
query = {
    "fmt": "ini",
    "key": keyword
}
params = parse.urlencode(query)
url = API + "?" + params
print("url=", url)

# ダウンロード --- (※4)
with req.urlopen(url) as r:
    b = r.read()
    data = b.decode('utf-8')
    print(data)
