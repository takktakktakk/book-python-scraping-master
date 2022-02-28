from bs4 import BeautifulSoup
import urllib.request as req
import re # 正規表現を使う時 --- (*1)

url = "https://itsalllight.stores.jp/"

with req.urlopen(url) as res:
  soup = BeautifulSoup(res, "html.parser")

# 正規表現でhrefからhttpsのものを抽出 --- (*2)
li = soup.find_all(href=re.compile(r"/item"))
for e in li:
  print("https://itsalllight.stores.jp" + e.attrs['href'])


