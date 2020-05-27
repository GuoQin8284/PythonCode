import time
from selenium import webdriver
ldriver=webdriver.Chrome()
ldriver.get("file:///C:/Users/GQ/Desktop/page1/%E6%B3%A8%E5%86%8CA.html")
ldriver.find_element_by_link_text("新浪").click()
time.sleep()
ldriver.close()