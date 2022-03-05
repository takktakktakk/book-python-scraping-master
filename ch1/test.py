
import re
import requests
from urllib.parse import urljoin

url = "https://ja.wikipedia.org/wiki/宇奈月温泉"
res2 = urljoin(url, "http://www.yaloo.com/wiki/ファイル:Pcs34560_IMG4098.JPG")

print(url)
print(res2)