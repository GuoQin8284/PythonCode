import time
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

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
# time.sleep(3)
# title=driver.find_elements_by_xpath("//*[contains(@text,'设')]")
# for a in title:
#     print(a.text)
# time.sleep(3)

# driver.start_activity("cn.goapk.market","com.anzhi.market.ui.MainActivity")
#
# driver.find_element_by_xpath("//*[@text='YY']").click()
#
# wait = WebDriverWait(driver,5,0.5).until(lambda x:x.find_element_by_xpath("//*[@text='YY']")).click()

driver.find_element_by_xpath("//*[@content-desc='搜索']").click()
search=driver.find_element_by_xpath("//*[@text='搜索…']")
search.send_keys("中国")
time.sleep(2)
search.clear()
time.sleep(2)
search.send_keys("hehe")
search.click()
time.sleep(3)
setting=driver.find_elements_by_id("android.widget.LinearLayout")
for i in setting:
    print(i.get_attribute("name"))
    print(i.get_attribute("package"))

driver.quit()