import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("file:///C:/Users/GQ/Desktop/%E6%B3%A8%E5%86%8CA.html")
driver.find_element_by_css_selector("#userA").send_keys("admin")
driver.find_element_by_css_selector("#passwordA").send_keys("123456")
driver.find_element_by_css_selector("#telA").send_keys("18000000000")
driver.find_element_by_css_selector("#emailA").send_keys("123@qq.com")
time.sleep(2)
driver.find_element_by_css_selector("button[value='注册A']").click()
time.sleep(3)
driver.quit()