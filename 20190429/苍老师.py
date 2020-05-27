import time

from selenium import webdriver

driver=webdriver.Chrome()
driver.get("http://172.16.64.1/WebAuth_auth.asp?ip=192.168.13.85&9313c")
driver.find_element_by_css_selector("#userName").send_keys("ruanjianceshi01")
driver.find_element_by_css_selector("#userPasswd").send_keys("19879164")
driver.find_element_by_css_selector("input[name='configSubmit']").click()
time.sleep(2)
driver.minimize_window()
driver.get("http://www.baidu.com")
time.sleep(4)
driver.find_element_by_css_selector("#kw").send_keys("苍井空")
driver.find_element_by_css_selector("#su").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='1']/h3/a/em").click()
time.sleep(5)
print("suoyou:",driver.current_window_handle)
driver.switch_to.window(driver.window_handles[1])
a = driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/div/div[1]/div[6]').text
print(a)
time.sleep(2)
driver.quit()