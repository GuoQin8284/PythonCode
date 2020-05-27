import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

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

print(driver.network_connection)

driver.set_network_connection(1)

print(driver.network_connection)


time.sleep(3)
driver.quit()