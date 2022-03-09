from selenium.webdriver import Chrome,ChromeOptions

url = "https://www.aozora.gr.jp/cards/000081/files/46268_23911.html"

# Firefoxをヘッドレスモードを有効にする --- (※1)
options = ChromeOptions()
options.add_argument('-headless')

# Firefoxを起動する --- (※2)
browser = Chrome(options=options)

# URLを読み込む --- (※3)
browser.get(url)

# 画面をキャプチャしてファイルに保存 --- (※4)
browser.save_screenshot("./ch2/website.png")
# ブラウザを終了 --- (※5)
browser.quit()

