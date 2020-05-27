from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("file:///C:/Users/GQ/Desktop/page1/%E6%B3%A8%E5%86%8CA.html")
driver.find_element_by_class_name("telA").send_keys("18012334560")
driver.find_element_by_class_name("emailA").send_keys("aed189")
time.sleep(3)
driver.close()