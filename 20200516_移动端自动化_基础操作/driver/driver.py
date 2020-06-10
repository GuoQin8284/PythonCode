from appium import webdriver


class SetupDriver():

    server_url = "127.0.0.1:4723/wd/hub"
    def __init__(self, appPackage = "com.android.launcher3", appActivity = "com.android.launcher3.Launcher", platformName = "android", platformVersion = "5.1", deviceName = "192.168.155.103:5555"):
        self.__setup = {}
        self.__setup["platformName"] = platformName
        self.__setup["platformVersion"] = platformVersion
        self.__setup["deviceName"] = deviceName
        self.__setup["appPackage"] = appPackage
        self.__setup["appActivity"] = appActivity
        self.__setup["unicodeKeyboard"] = True
        self.__setup["resetKeyboard"] = True
    def setupDriver(self):
        driver = webdriver.Remote(self.server_url,self.__setup)
        driver.implicitly_wait(20)
        return driver