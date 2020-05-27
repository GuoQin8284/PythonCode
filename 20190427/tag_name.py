import time
from selenium import webdriver
# 创建对象：
tdriver=webdriver.Chrome()
tdriver.get("file:///C:/Users/GQ/Desktop/page1/%E6%B3%A8%E5%86%8CA.html")
tdriver.find_element_by_tag_name("input").send_keys("123455")
time.sleep(3)
tdriver.close()