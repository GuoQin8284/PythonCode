import time
from selenium import webdriver

dr = webdriver.Chrome()
dr.get("file:///C:/Users/GQ/Desktop/page1/%E6%B3%A8%E5%86%8CA.html")
time.sleep(2)
dr.execute_script("window.scrollTo(0,100000)")
time.sleep(2)
dr.quit()