import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

dr = webdriver.Chrome()
dr.get("file:///C:/Users/GQ/Desktop/page1/%E6%B3%A8%E5%86%8CA.html")
try:
    print("start:",time.time())
    element = WebDriverWait(dr,10,0.1).until(lambda x:x.find_element_by_css_selector("#userA1"))
    element.send_keys("admin")
except:
    print("end",time.time())
