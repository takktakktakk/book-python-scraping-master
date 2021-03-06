# 作詞掲示板にログインしてお気に入りの詞を取得する
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# ユーザー名とパスワードの指定 --- (※1)
USER = "JS-TESTER"
PASS = "ipCU12ySxI"

# セッションを開始 --- (※2)
session = requests.session()
# リクエストヘッダーを設定しないとスクレイピングとバレるため偽装。
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36" ,"Accept": "text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,image/apng,*/*;q=0.8"}

# ログイン --- (※3)
login_info = {
    "username_mmlbbs6": USER,  # ユーザー名を指定
    "password_mmlbbs6": PASS,  # パスワードを指定
    "back": "index.php",       # ログイン時に指定する値
    "mml_id": "0"              # ログイン時に指定する値
}
url_login = "https://uta.pw/sakusibbs/users.php?action=login&m=try"
res = session.post(url_login, headers = headers, data=login_info)
try:
    res.raise_for_status()
except RequestException as e:
    print(e.response.text)# エラーならここで例外を発生させる

# マイページのURLをピックアップする --- (※4)
soup = BeautifulSoup(res.text, "html.parser")
a = soup.select_one(".islogin a")
if a is None:
    print("マイページが取得できませんでした")
    quit()
# 相対URLを絶対URLに変換
url_mypage = urljoin(url_login, a.attrs["href"])
print("マイページ=", url_mypage)

# マイページにアクセス --- (※5)
res = session.get(url_mypage)
try:
    res.raise_for_status()
except RequestException as e:
    print(e.response.text)

# お気に入りの詞のタイトルを列挙 --- (※6)
soup = BeautifulSoup(res.text, "html.parser")
links = soup.select("#favlist li > a")
for a in links:
    href = a.attrs["href"]
    title = a.get_text()
    print("-", title, ">", href)



