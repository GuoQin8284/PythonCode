from appium import webdriver


setup = {}

setup["platformName"] = "android"
setup["platformVersion"] = "5.1"
setup["deviceName"] = "192.168.155.103:5555"
setup["appPackage"] = "com.cyanogenmod.filemanager"
setup["appActivity"] = "com.cyanogenmod.filemanager.activities.NavigationActivity"
setup["unicodeKeyboard"] = True
setup["resetKeyboard"] = True
setup["noReset"] = True
setup["automationName"] = "Uiautomator2"


driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=setup)
driver.press_keycode(4)
text = driver.find_element_by_xpath("//*[contains(@text,'即可退出')]")
print(text.text)