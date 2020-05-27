import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("file:///C:/Users/GQ/Desktop/page1/%E6%B3%A8%E5%86%8CA.html")
# driver.find_element_by_xpath("//*[text()='新浪']").click()
# driver.find_element_by_xpath("//*[contains(@placeholder,'电子邮箱')]").send_keys("1@126.com")
driver.find_element_by_xpath("//*[starts-with(@placeholder,'请输入电子')]").send_keys("1@qq.com")
time.sleep(3)
driver.close()