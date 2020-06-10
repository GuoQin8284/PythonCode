from appium import webdriver

desired_caps={
    "platformName": "android",
    "platformVerison": "5.1",
    "deviceName": "192.168.155.103:5555",
    "appPackage": "com.android.browser",
    "appActivity": "com.android.browser.BrowserActivity",
    "unicodeKeyboard": True,
    "resetKeyboard": True,
    "noReset": False
}

driver = webdriver.Remote(command_executor="127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)
driver.find_element_by_id("com.android.browser:id/url").send_keys("www.baidu.com")
driver.press_keycode(66)
print(driver.contexts)
driver.switch_to.context(driver.contexts[-1])
driver.find_element_by_id("index-kw").send_keys("10086")
driver.find_element_by_id("index-bn").click()