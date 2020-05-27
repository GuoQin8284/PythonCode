import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://localhost")
driver.find_element_by_link_text("登录").click()
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()
time.sleep(2)
driver.quit()