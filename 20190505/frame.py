import time
from selenium import webdriver

dr = webdriver.Chrome()
dr.implicitly_wait(10)
dr.maximize_window()
dr.get("file:///C:/Users/GQ/Desktop/page1/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html")
dr.find_element_by_id("user").send_keys("admin")
time.sleep(2)
dr.switch_to.frame("idframe1")
dr.find_element_by_id("userA").send_keys("admin")
dr.switch_to.default_content()
dr.switch_to.frame("myframe2")
dr.find_element_by_id("userB").send_keys("admin")
time.sleep(2)
dr.quit()
