import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("file:///C:/Users/GQ/Desktop/page1/%E6%B3%A8%E5%86%8CA.html")
driver.find_element_by_css_selector("input[name='telA']").send_keys('12345612345')
time.sleep(3)
driver.find_element_by_css_selector('button').click()
time.sleep(3)
driver.close()