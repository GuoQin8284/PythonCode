from appium import webdriver


class SetupConfig():

    def init_driver(self):
        setup_config={}

        setup_config["platformName"]="android"
        setup_config["platformVersion"]=5.1
        setup_config["deviceName"]="192.168.149.101:5555"
        setup_config["appPackage"]="com.android.contacts"
        setup_config["appActivity"]=".activities.PeopleActivity"
        setup_config["unicodekeyboard"]=True
        setup_config["resetkeyboard"]=True

        return webdriver.Remote("http://localhost:4723/wd/hub",setup_config)