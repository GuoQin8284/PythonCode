import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("file:///C:/Users/GQ/Desktop/page1/%E6%B3%A8%E5%86%8CA.html")
driver.find_element_by_css_selector("#userA").send_keys("123456789")
driver.find_element_by_xpath('//input[@id="passwordA"]').send_keys("123456")
driver.find_element_by_css_selector('.telA').send_keys('1234567890')
driver.find_element_by_css_selector(".emailA").send_keys('123@qq.com')
time.sleep(3)
driver.find_element_by_css_selector("#userA").clear()
time.sleep(3)
driver.find_element_by_css_selector("input[name='userA']").send_keys('098765431')

time.sleep(3)
driver.quit()