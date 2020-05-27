from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("file:///C:/Users/GQ/Desktop/page1/%E6%B3%A8%E5%86%8CA.html")
user=driver.find_element_by_id("userA")
user.send_keys("admin")
time.sleep(2)
password= driver.find_element_by_id("passwordA")
password.send_keys("1233456")


time.sleep(4)
driver.quit()