import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("file:///C:/Users/GQ/Desktop/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html")
# 填写注册实例页面信息
driver.find_element_by_css_selector("#user").send_keys("admin")
driver.find_element_by_css_selector("#password").send_keys("123456")
driver.find_element_by_css_selector("#tel").send_keys("18000000000")
driver.find_element_by_css_selector("#email").send_keys("123@qq.com")

# 点击注册A页面
driver.find_element_by_link_text("注册A网页").click()
# 切换到新窗口
driver.switch_to.window(driver.window_handles[-1])
# 填写注册A页面信息
driver.find_element_by_css_selector("#userA").send_keys("admin")
driver.find_element_by_css_selector("#passwordA").send_keys("123456")
driver.find_element_by_css_selector("#telA").send_keys("18000000000")
driver.find_element_by_css_selector("#emailA").send_keys("123@qq.com")
# 切换到注册实例
driver.switch_to.window(driver.window_handles[-2])

# 点击注册B页面
driver.find_element_by_link_text("注册B网页").click()
driver.switch_to.window(driver.window_handles[-1])
# 填写注册B页面信息
driver.find_element_by_css_selector("#userB").send_keys("admin")
driver.find_element_by_css_selector("#passwordB").send_keys("123456")
driver.find_element_by_css_selector("#telB").send_keys("18000000000")
driver.find_element_by_css_selector("#emailB").send_keys("123@qq.com")

#填写完毕，等待3S
time.sleep(3)
# 关闭浏览器
driver.quit()