import time

from driver.driver import SetupDriver

launcher = "com.android.launcher3","com.android.launcher3.Launcher"
setting = "com.android.settings","com.android.settings.Settings"

driver = SetupDriver(platformVersion="8.0",appPackage=launcher[0],appActivity=launcher[1]).setupDriver()

driver.start_activity(setting[0],setting[1])

network_button = driver.find_element_by_xpath("//*[@text='网络和互联网']")

audio_button = driver.find_element_by_xpath("//*[@text='声音']")

network_point = (290,400)

application_point = (260,770)

# driver.swipe(application_point[0],application_point[1],network_point[0],network_point[1],duration=1)
#
driver.drag_and_drop(audio_button,network_button)

# driver.scroll(audio_button,save_button)

time.sleep(3)

driver.quit()