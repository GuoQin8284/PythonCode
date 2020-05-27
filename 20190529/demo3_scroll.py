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

time.sleep(1)

frist_element=driver.find_element_by_xpath("//*[@text='更多']")
second_element=driver.find_element_by_xpath("//*[@text='存储']")
driver.scroll(second_element,frist_element)

time.sleep(2)

driver.drag_and_drop(frist_element,second_element)

cpck=driver.current_package
catv=driver.current_activity

print(frist_element.get_attribute("text"))
print(frist_element.get_attribute("className"))
print(second_element.get_attribute("resourceId"))

driver.quit()