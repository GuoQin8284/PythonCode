from appium import webdriver


def setupDriver(platformName="android", platformVersion="5.1", deviceName="192.168.33.101:5555",
                appPackage="com.android.settings", appActivity="com.android.settings.Settings",
                url="127.0.0.1:4723/wd/hub"):
    desired_caps = {
        "platformName": platformName,
        "platformVersion": platformVersion,
        "deviceName": deviceName,
        "appPackage": appPackage,
        "appActivity": appActivity,
        "unicodeKeyboard": True,
        "resetKeyboard": True,
        "noReset": False
    }
    driver = webdriver.Remote(desired_capabilities=desired_caps, command_executor=url)
    return driver
