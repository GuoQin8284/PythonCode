# 练习1

import time
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

setup_config={}
setup_config["platformName"]="android"
setup_config["platformVersion"]="5.1"
setup_config["deviceName"]="192.168.149.101:5555"
setup_config["appPackage"]="com.android.settings"
setup_config["appActivity"]=".Settings"
setup_config["unicodeKeyboard"]=True
setup_config["resetKeyboard"]=True

driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",setup_config)

driver.implicitly_wait(10)

driver.find_element_by_xpath("//*[@content-desc='搜索']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@text='搜索…']").send_keys("123abc")
time.sleep(1)
driver.find_element_by_xpath("//*[@content-desc='收起']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@content-desc='搜索']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@text='搜索…']").send_keys("qwertyuiop")
time.sleep(1)
driver.find_element_by_xpath("//*[@content-desc='收起']").click()

get_list=driver.find_elements_by_xpath("//*[@text='WLAN']")
# a = 1
# for i in get_list:
#     if i.text=="WLAN":
#         print("该页面包含WLAN")
#         break
#     elif a==len(get_list):
#         print("该页面不包含WLAN")
#         a=0
#     a = a + 1

if len(get_list):
    print("该页面包含WLAN")
else:
    print("该页面不包含WLAN")

time.sleep(2)
driver.quit()
