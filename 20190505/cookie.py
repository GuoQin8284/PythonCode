import time
from selenium import webdriver

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
# driver.get("http://172.16.64.1/WebAuth_auth.asp?ip=192.168.13.85&9313c")
# driver.find_element_by_css_selector("#userName").send_keys("ruanjianceshi01")
# driver.find_element_by_css_selector("#userPasswd").send_keys("19879164")
# driver.find_element_by_css_selector("input[name='configSubmit']").click()
driver.get("http://www.baidu.com")
time.sleep(4)
print(driver.get_cookies())
driver.add_cookie({"name":"BDUSS","value":"lU4cjVkVU1VN25xUE04ZDVFbE02SDVxN35GTnZhWG0yMzdFMEtqQmY5MUxaZlpjRUFBQUFBJCQAAAAAAAAAAAEAAADr8ilcR3VvUWluODI4NAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEvYzlxL2M5cT"})
# time.sleep(1)
driver.refresh()
# time.sleep(2)
# driver.quit()