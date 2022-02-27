from bs4 import BeautifulSoup 
import urllib.request as req

url = "https://www.aozora.gr.jp/index_pages/person148.html"

with req.urlopen(url) as res:
    soup = BeautifulSoup(res, "html.parser")

li_list = soup.select("ol > li:nth-of-type(1)")
for li in li_list:
    a = li.a
    if a != None:
        name = a.string
        href = a.attrs["href"]
        print(name, ">", href)

