import time
from selenium import webdriver

driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()
driver.find_element_by_id("kw").send_keys("hello")
time.sleep(3)
driver.find_element_by_id("su").click()