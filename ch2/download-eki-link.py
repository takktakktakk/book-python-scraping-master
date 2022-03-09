from urllib.parse import *
from urllib.request import *
from bs4 import BeautifulSoup
import os, os.path, time
import random

# リンクを抽出する --- (※1)
html = open("ch2/eki-link.html", encoding="utf-8").read()
soup = BeautifulSoup(html, "html.parser")
links = soup.select("a[href]")
result = []
for a in links:
    href = a.attrs["href"]
    title = a.string
    result.append((title, href))

# リンク先をダウンロードする --- (※2)
savepath = "./ch2/DL";
if not os.path.exists(savepath):
    os.mkdir(savepath)

for title, url in result:
    path = savepath + "/" + url + ".html"
    # 相対URLを絶対URLに変換
    a_url = urljoin("http://example.com", url)
    print("download=" + a_url)
    # ここでダウンロードを行う
    # urlretrieve(a_url, path)
    ra = random.uniform(1, 2)
    time.sleep(ra)

