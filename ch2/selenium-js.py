# coding:utf-8
from selenium.webdriver import Chrome,ChromeOptions



options =ChromeOptions()
options.add_argument('-headless')
browser = Chrome(options=options)

r = browser.execute_script("return 100 + 50")
print(r)