from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

dr = webdriver.Chrome()
dr.get("file:///C:/Users/GQ/Desktop/page1/%E6%B3%A8%E5%86%8CA.html")
element = WebDriverWait(dr,10,0.1).until(lambda x : x.find_element_by_id("userA"))
element.send_keys("admin")