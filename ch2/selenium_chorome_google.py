from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = ChromeOptions()
# ヘッドレスモードを有効にする（次の行をコメントアウトすると画面が表示される）。
options.add_argument('--headless')
# ChromeのWebDriverオブジェクトを作成する。
driver = Chrome(options=options)

# Googleのトップ画面を開く。
driver.get('https://www.google.co.jp/')

# タイトルに'Google'が含まれていることを確認する。
assert 'Google' in driver.title

# 検索語を入力して送信する。
input_element = driver.find_element(by=By.XPATH, value="//input[@name='q']")
input_element.send_keys('Python')
input_element.send_keys(Keys.RETURN)

# タイトルに'Python'が含まれていることを確認する。
assert 'Python' in driver.title

# スクリーンショットを撮る。
driver.save_screenshot('chrome_search_results.png')

# 検索結果を表示する。
for a in driver.find_elements(by=By.TAG_NAME, value="a"):
    print(a.text)
    print(a.get_attribute('href'))

driver.quit()  # ブラウザーを終了する。