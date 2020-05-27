import time

from driver.driver import SetupDriver

launcher = "com.android.launcher3","com.android.launcher3.Launcher"
setting = "com.android.settings","com.android.settings.Settings"
driver = SetupDriver(platformVersion="8.0",appPackage=launcher[0],appActivity=launcher[1]).setupDriver()

driver.press_keycode(82)  #按下菜单键
time.sleep(2)

driver.press_keycode(3)   #按下home键
time.sleep(2)

driver.press_keycode(4)   #按下返回键
time.sleep(2)

driver.quit()