import time

from driver.driver import SetupDriver

launcher = "com.android.launcher3","com.android.launcher3.Launcher"
setting = "com.android.settings","com.android.settings.Settings"
driver = SetupDriver(platformVersion="8.0",appPackage=launcher[0],appActivity=launcher[1]).setupDriver()

driver.open_notifications()  #打开通知栏
time.sleep(3)
driver.press_keycode(4)     #通过返回键关闭通知栏

driver.quit()