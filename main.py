import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome(executable_path="./drivers/chromedriver")
browser.get('https://www.google.co.in')
time.sleep(5)
browser.quit()
