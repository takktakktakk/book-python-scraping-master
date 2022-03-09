# 参考サイト：https://qiita.com/seigot/items/475da9b3701cea8fb384
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = ChromeOptions()
# ヘッドレスモードを有効にする（次の行をコメントアウトすると画面が表示される）。
options.headless = True
# ChromeのWebDriverオブジェクトを作成する。
driver = Chrome(options=options)

# Googleのトップ画面を開く。

driver.get('https://www.google.co.jp/')

# タイトルに'Google'が含まれていることを確認する。
assert 'Google' in driver.title, "タイトル[{}]には[{}]が含まれていません。".format(driver.title, "Python")

# 検索語を入力して送信する。
input_element = driver.find_element(by=By.XPATH, value="//input[@name='q']")
input_element.send_keys('Python')
input_element.send_keys(Keys.RETURN)

# タイトルに'Python'が含まれていることを確認する。
assert 'Python' in driver.title, "タイトル[{}]には[{}]が含まれていません。".format(driver.title, "Python")

# スクリーンショットを撮る。
driver.save_screenshot('ch2/selenium_chrome_google.png')

# 検索結果を表示する。
for elem_h3 in driver.find_elements(by = By.XPATH, value = '//a/h3'):
    elem_a = elem_h3.find_element(by = By.XPATH, value = '..')
    print(elem_h3.text)
    print(elem_a.get_attribute('href') + "\n")

driver.close()  # ブラウザーを終了する。