import time
from appium.webdriver.common.touch_action import TouchAction

from driver.driver import SetupDriver

launcher = "com.android.launcher3","com.android.launcher3.Launcher"
setting = "com.android.settings","com.android.settings.Settings"
network_point = (290,400)

driver = SetupDriver(platformVersion="8.0",appPackage=launcher[0],appActivity=launcher[1]).setupDriver()
driver.start_activity(setting[0],setting[1])

network_button = driver.find_element_by_xpath("//*[@text='网络和互联网']")
audio_button = driver.find_element_by_xpath("//*[@text='声音']")

def find_text_ele(ele):
    return driver.find_element_by_xpath("//*[@text='{}']".format(ele))

touchAction = TouchAction(driver)
# touchAction.press(el = network_button).perform()

# touchAction.tap(element=network_button).perform()

# touchAction.press(el=network_button).wait(3000).release().perform()

# touchAction.long_press(el=network_button,duration = 5000).perform()

# touchAction.tap(element=network_button).perform().perform()
# touchAction.tap(element=find_text_ele("WLAN")).perform()
# touchAction.long_press(el=find_text_ele("AndroidWifi"),duration=5000).perform()

driver.drag_and_drop(origin_el=find_text_ele("电池"),destination_el=find_text_ele("网络和互联网"))

touchAction.tap(element=find_text_ele("安全性与位置信息")).perform()
touchAction.tap(element=find_text_ele("屏幕锁定")).perform()
touchAction.tap(element=find_text_ele("图案")).perform()
time.sleep(2)
touchAction.press(x=267,y=854).\
    move_to(x=808,y=874).\
    move_to(x=814,y=1405).release().perform()

touchAction.tap(element=find_text_ele("继续")).perform()

touchAction.press(x=267,y=854).\
    move_to(x=808,y=874).\
    move_to(x=814,y=1405).release().perform()

touchAction.tap(element=find_text_ele("确认")).perform()
time.sleep(5)
driver.quit()