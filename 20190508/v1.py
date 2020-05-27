import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("http://localhost")
# 账号错误
driver.find_element_by_link_text("登录").click()
driver.find_element_by_id("username").send_keys("13000000000")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("verify_code").send_keys("8888")
driver.find_element_by_link_text("登    录").click()
print(driver.switch_to.alert.text)

# 密码错误
driver.find_element_by_link_text("登录").click()
driver.find_element_by_id("username").send_keys("18012345678")
driver.find_element_by_id("password").send_keys("123321")
driver.find_element_by_id("verify_code").send_keys("8888")
driver.find_element_by_link_text("登    录").click()
print(driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[2]').text)


time.sleep(3)
driver.quit()