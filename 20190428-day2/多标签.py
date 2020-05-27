import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("file:///C:/Users/GQ/Desktop/page1/%E6%B3%A8%E5%86%8CA.html")
driver.find_element_by_xpath("//input[@class='login' and @name='user']").send_keys("hahaha")
time.sleep(2)
driver.close()