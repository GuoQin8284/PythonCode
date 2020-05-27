
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

driver.open_notifications()
time.sleep(2)
driver.swipe(100,600,100,300)

time.sleep(3)
driver.quit()