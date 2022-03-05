# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
import chromedriver_binary


options =ChromeOptions()
options.add_argument('-headless')
browser = Chrome(options=options)

r = browser.execute_script("return 100 + 50")
print(r)