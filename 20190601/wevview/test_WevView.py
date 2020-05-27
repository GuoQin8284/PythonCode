from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

setup_config={}
setup_config["platformName"]="android"
setup_config["platformVersion"]="5.1"
setup_config["deviceName"]="192.168.149.101:5555"
setup_config["appPackage"]="com.android.browser"
setup_config["appActivity"]=".BrowserActivity"
setup_config["unicodeKeyboard"]=True
setup_config["resetKeyboard"]=True
setup_config["automationName"]="Uiautomator2"

driver=webdriver.Remote("http://localhost:4723/wd/hub",setup_config)
driver.implicitly_wait(10)
# search=driver.find_element_by_xpath("//*[@resourse-id='com.android.browser:id/url' and @class='android.widget.EditText']")
# print(search)
TouchAction(driver).tap(x=141,y=82).perform().clear()
# search.send_keys("http://www.baidu.com")
TouchAction(driver).tap(x=39,y=79).perform()
driver.switch_to.context("WEBVIEW_com.android.browser")
driver.find_elements_by_id("index-kw").send_keys("习近平")