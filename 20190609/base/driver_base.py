from appium import webdriver


def init_driver(no_reset=True):

    setup_config={}
    setup_config["platfromName"]="android"
    setup_config["platfromVersion"]=5.1
    setup_config["deviceName"]="1"
    setup_config["appPackage"]="com.android.settings"
    setup_config["appActivity"]=".Settings"
    setup_config["unicodekeyboard"]=True
    setup_config["resetkeyboard"]=True
    setup_config['automationName'] = 'Uiautomator2'
    setup_config['noReset'] = no_reset

    driver=webdriver.Remote("http://localhost:4723/wd/hub",setup_config)
    driver.swipe()
    return driver