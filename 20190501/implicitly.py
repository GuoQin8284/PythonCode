import time
from selenium import webdriver

dr = webdriver.Chrome()
# dr.implicitly_wait(10)
dr.get("file:///C:/Users/GQ/Desktop/page1/%E6%B3%A8%E5%86%8CA.html")
print("in:",time.time())
dr.find_element_by_id("userA").send_keys("admin")
print("out:",time.time())