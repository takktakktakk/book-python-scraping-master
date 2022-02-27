from bs4 import BeautifulSoup
import urllib.request as req

url = "https://api.aoikujira.com/zip/xml/1500042"

# urlopen()でデータを取得 --- (※1)
with req.urlopen(url) as req:
    # BeautifulSoupで解析 --- (※2)
    soup = BeautifulSoup(req, "html.parser")
    print(type(soup))

# 任意のデータを抽出 --- (※3)
ken = soup.find("ken").string
shi = soup.find("shi").string
cho = soup.find("cho").string
print(ken, shi, cho)
