import time
from selenium import webdriver

dr = webdriver.Chrome()

dr.get("file:///C:/Users/GQ/Desktop/page1/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html")

dr.switch_to.frame(dr.find_element_by_xpath("//iframe[@id='idframe1']"))

dr.find_element_by_id("userA").send_keys("admin")
time.sleep(2)
dr.switch_to.default_content()
dr.switch_to.frame("myframe2")
dr.find_element_by_id("userB").send_keys("admin")
time.sleep(2)
dr.quit()