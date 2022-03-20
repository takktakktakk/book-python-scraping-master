# 画像データを取得
import requests
res = requests.get("https://uta.pw/shodou/img/3/3.png")

# バイナリ形式でデータを得て保存
with open("./ch2/test.png", "wb") as file:
    file.write(res.content)

print("saved")

