from time import sleep, time

import time
from appium import webdriver

setup_config={}
setup_config["platformName"]="android"
setup_config["platformVersion"]="5.1"
setup_config["deviceName"]="192.168.149.101:5555"
setup_config["appPackage"]="com.android.settings"
setup_config["appActivity"]=".Settings"
setup_config["unicodekeyboard"]=True
setup_config["resetkeyboard"]=True

driver=webdriver.Remote("http://localhost:4723/wd/hub",setup_config)
driver.implicitly_wait(10)
time.sleep(3)
driver.swipe(100, 300, 100, 100)
time.sleep(2)

driver.quit()
