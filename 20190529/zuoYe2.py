# 练习1

import time
from appium import webdriver

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

driver.find_element_by_xpath("//*[@text='更多']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@class='android.widget.Switch' and @resource-id='android:id/switchWidget']").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@class='android.widget.Switch' and @resource-id='android:id/switchWidget']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@text='移动网络']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@text='首选网络类型']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@text='2G']").click()

time.sleep(3)
driver.quit()
