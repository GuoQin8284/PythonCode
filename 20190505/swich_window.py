import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

dr = webdriver.Chrome()
dr.implicitly_wait(10)
dr.get("file:///C:/Users/GQ/Desktop/page1/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html")
dr.find_element_by_id("ZCA").click()
print("current:",dr.current_window_handle)
print("suoyou:",dr.window_handles)
time.sleep(1)
dr.switch_to.window(dr.window_handles[1])
a = dr.find_element_by_id("userA")
a.send_keys("admin")
a.send_keys(Keys.CONTROL,"a")
a.send_keys(Keys.CONTROL,"c")
dr.find_element_by_id("passwordA").send_keys(Keys.CONTROL,"v")
time.sleep(2)
b=ActionChains(dr)
b.context_click(dr.find_element_by_id("userA")).perform()
time.sleep(2)
dr.quit()
