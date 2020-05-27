import time
from selenium import webdriver
from selenium.webdriver import ActionChains
dr = webdriver.Chrome()
dr.get("file:///C:/Users/GQ/Desktop/page1/drag.html")
time.sleep(1)
ActionChains(dr).drag_and_drop(dr.find_element_by_css_selector("#div1"),dr.find_element_by_css_selector("#div2")).perform()