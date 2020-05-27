from selenium import webdriver
from selenium.webdriver import ActionChains
import time

dr = webdriver.Chrome()
dr.get("http://localhost")
dr.maximize_window()
time.sleep(4)
ActionChains(dr).move_to_element(dr.find_element_by_xpath("//a[text()='电脑']")).click(dr.find_element_by_xpath("//a[text()='CPU']")).perform()
time.sleep(3)
time.sleep(4)
dr.quit()