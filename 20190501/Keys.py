import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

dr = webdriver.Chrome()
dr.get("file:///C:/Users/GQ/Desktop/page1/%E6%B3%A8%E5%86%8CA.html")
time.sleep(2)
element = dr.find_element_by_xpath("//input[@id='userA']")
time.sleep(2)
element.send_keys("admin1")
time.sleep(2)
element.send_keys(Keys.BACKSPACE)
time.sleep(2)
element.send_keys(Keys.CONTROL,"a")
time.sleep(2)
element.send_keys(Keys.CONTROL,"c")
time.sleep(2)
dr.find_element_by_id("passwordA").send_keys(Keys.CONTROL,"v")
time.sleep(3)
dr.quit()
