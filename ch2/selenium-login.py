from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

USER = "JS-TESTER"
PASS = "ipCU12ySxI"

# Chromeのドライバを得る --- (※1)
options = ChromeOptions()
options.add_argument('-headless')
browser = Chrome(options=options)

# ログインページにアクセス --- (※2)
url_login = "https://uta.pw/sakusibbs/users.php?action=login"
browser.get(url_login)
print("ログインページにアクセスしました")

# テキストボックスに文字を入力 --- (※3)
e = browser.find_element(by=By.ID, value="user")
e.clear()
e.send_keys(USER)
e = browser.find_element(by=By.ID, value="pass")
e.clear()
e.send_keys(PASS)
# フォームを送信 --- (※4)
frm = browser.find_element(by=By.XPATH, value="//form")
frm.submit()
print("情報を入力してログインボタンを押しました")
# ページのロード完了まで待機 --- (※5)
WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".islogin")))

# マイページのURLを得る --- (※6)
a = browser.find_element(by=By.CSS_SELECTOR, value=".islogin a")
url_mypage = a.get_attribute('href')
print("マイページのURL=", url_mypage)
# マイページを表示 --- (※7)
browser.get(url_mypage)
browser.execute_script('document.getElementById("mmlist").scrollIntoView(true)')

browser.save_screenshot("./ch2/selenium_login.png")

# お気に入りのタイトルを列挙 --- (※8)
links = browser.find_elements(by=By.CSS_SELECTOR, value="#favlist li > a")
for a in links:
    href = a.get_attribute('href')
    title = a.text
    print("-", title, ">", href)


browser.quit() 
