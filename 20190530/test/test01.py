import os
import time
from appium import webdriver
import pytest
from appium.webdriver.common.touch_action import TouchAction


class TestLogin():
    def setup_class(self):
        setup_config = {}
        setup_config["platformName"] = "android"
        setup_config["platformVersion"] = "5.1"
        setup_config["deviceName"] = "192.168.149.101:5555"
        setup_config["appPackage"] = "com.android.settings"
        setup_config["appActivity"] = ".Settings"
        setup_config["unicodeKeyboard"] = True
        setup_config["resetKeyboard"] = True
        self.driver=webdriver.Remote("http://localhost:4723/wd/hub",setup_config)
        self.driver.implicitly_wait(5)

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.run(1)
    def test_01_setting(self):
        self.driver.swipe(100,600,100,200)
        a = self.driver.find_elements_by_xpath("//*[@text='存储']")
        print(len(a))
        assert len(a)

    @pytest.mark.run(2)
    def test_02_search(self):
        first = self.driver.find_element_by_xpath("//*[@text='用户']")
        second = self.driver.find_element_by_xpath("//*[@text='存储']")

        print(first)
        print(second)
        time.sleep(1)
        self.driver.scroll(second,first)
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@content-desc='搜索']").click()
        d = self.driver.find_element_by_xpath("//*[@class='android.widget.EditText' and @resource-id='android:id/search_src_text']")
        d.send_keys("abc")
        assert d.text=="abc"

    @pytest.mark.run(3)
    def test_03_tap(self):
        touch=TouchAction(self.driver)
        touch.tap(x=43,y=81).perform()
        time.sleep(1)
        touch.tap(self.driver.find_element_by_xpath("//*[@text='WLAN']")).perform()
        time.sleep(1)
        touch.press(x=158,y=247,).wait(2).perform()
        time.sleep(1)
        if self.driver.find_elements_by_xpath("//*[@text='取消保存网络']"):
            self.driver.press_keycode(4)
        else:
            touch.tap(self.driver.find_element_by_xpath("//*[@text='连接到网络']")).perform()
        time.sleep(1)
        self.driver.press_keycode(4)
        time.sleep(1)
        # self.driver.get_screenshot_as_file(os.getcwd()+os.sep+"./screen.png")
        self.driver.get_screenshot_as_file(r"D:\python code\20190530\test\screenshot\screen.png")
        time.sleep(1)
        self.driver.open_notifications()
        time.sleep(1)
        self.driver.swipe(200,600,200,100)
        time.sleep(1)
        touch.tap(x=43,y=81).perform()
        time.sleep(1)
        self.driver.press_keycode(4)
        print("*"*100)
        time.sleep(2)
        print("current_package",self.driver.current_package)
        assert self.driver.current_package=="com.android.launcher3"
