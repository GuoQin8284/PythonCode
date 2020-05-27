import time
from selenium import webdriver

xdriver = webdriver.Chrome()
xdriver.get("file:///C:/Users/GQ/Desktop/page1/%E6%B3%A8%E5%86%8CA.html")
xdriver.find_element_by_xpath("//input[@name='userA']").send_keys("admin")
xdriver.find_element_by_xpath('//input[@placeholder="请输入密码"]').send_keys("123456")
time.sleep(3)
xdriver.quit()