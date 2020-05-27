from driver.driver import SetupDriver

launcher = "com.android.launcher3","com.android.launcher3.Launcher"
setting = "com.android.settings","com.android.settings.Settings"
driver = SetupDriver(platformVersion="8.0",appPackage=launcher[0],appActivity=launcher[1]).setupDriver()

netStatus = driver.network_connection # 获取当前网络状态
print(netStatus)


setNet = driver.set_network_connection(4) #设置当前网络状态为
print(setNet)
