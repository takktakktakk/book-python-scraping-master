# ライブラリの取り込み --- (※1)
import urllib.request

# URLと保存パスを指定
url = "https://uta.pw/shodou/img/28/214.png"
savename = "test.png"

# ダウンロード --- (※2)
urllib.request.urlretrieve(url, savename)#あまり推奨されない → DL中断で不完全ファイルが作成される
print("保存しました")

