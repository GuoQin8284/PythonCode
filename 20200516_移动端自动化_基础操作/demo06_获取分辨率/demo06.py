from driver.driver import SetupDriver

launcher = "com.android.launcher3","com.android.launcher3.Launcher"
setting = "com.android.settings","com.android.settings.Settings"
driver = SetupDriver(platformVersion="8.0",appPackage=launcher[0],appActivity=launcher[1]).setupDriver()
driver.start_activity(setting[0],setting[1])

size = driver.get_window_size()
print(size)