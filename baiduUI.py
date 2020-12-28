import time

from selenium import webdriver

driver = webdriver.Chrome()
url = "https://www.baidu.com"
driver.get(url=url)
driver.maximize_window()
driver.implicitly_wait(30)
time.sleep(2)

driver.quit()

