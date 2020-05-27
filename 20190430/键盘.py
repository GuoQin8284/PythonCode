import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
dr = webdriver.Chrome()
dr.implicitly_wait(30)
dr.get("file:///C:/Users/GQ/Desktop/page1/%E6%B3%A8%E5%86%8CA.html")
dr.find_element_by_css_selector("#userA").send_keys("admin")
dr.find_element_by_css_selector("#userA").send_keys(Keys.BACKSPACE)
time.sleep(1)
dr.find_element_by_css_selector("#userA").send_keys(Keys.TAB)
dr.find_element_by_css_selector("#userA").send_keys(Keys.CONTROL,"a")
dr.find_element_by_css_selector("#userA").send_keys(Keys.CONTROL,"c")
dr.find_element_by_css_selector("#passwordA").send_keys(Keys.CONTROL,"v")







