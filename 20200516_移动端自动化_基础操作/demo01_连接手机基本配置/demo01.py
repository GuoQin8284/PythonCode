import time
from appium import webdriver

setup = {}
setup["platformName"] = "android"
setup["platformVersion"] = "5.1"
setup["deviceName"] = "192.168.155.103:5555"
setup["appActivity"] = "com.android.launcher3.Launcher"
setup["appPackage"] = "com.android.launcher3"

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",setup)

if driver.is_app_installed("com.wandoujia.phoenix2"):
    print("豌豆荚应用已安装，正在卸载")
    driver.remove_app("com.wandoujia.phoenix2")
    if driver.is_app_installed("com.wandoujia.phoenix2") is False:
        print("豌豆荚已成功卸载")
else:
    print("豌豆荚应用不存在，正在安装")
    driver.install_app(r"F:\apk\Wandoujia_2891094_web_seo_baidu_homepage.apk")
    if driver.is_app_installed("com.wandoujia.phoenix2"):
        print("豌豆荚应用已成功安装，正在打开")
        driver.start_activity("com.wandoujia.phoenix2","com.pp.assistant.activity.PPMainActivity")

time.sleep(5)

driver.close_app()
print(driver.current_package)
print(driver.current_activity)

driver.quit()