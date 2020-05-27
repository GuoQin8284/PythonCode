import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("file:///C:/Users/GQ/Desktop/page1/%E6%B3%A8%E5%86%8CA.html")
driver.find_element_by_xpath("//p[@id='p1']/input").send_keys('哈哈哈哈')
time.sleep(3)
driver.quit()