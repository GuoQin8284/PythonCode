import time
from selenium import webdriver

dr=webdriver.Chrome()
dr.get("file:///C:/Users/GQ/Desktop/page1/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html")
dr.find_element_by_link_text("注册A页面").click()
print("dangqian:",dr.current_window_handle)
print("suoyou:",dr.window_handles)
print("-"*50)
dr.switch_to.window(dr.window_handles[1])
dr.find_element_by_id("userA").send_keys("admin")
time.sleep(2)
dr.quit()