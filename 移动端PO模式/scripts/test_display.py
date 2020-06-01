import time

from base.setup_driver import setupDriver
from page.display_page import DisplayPage
from page.setting_page import SettingPage


class TestDisplay():

    def setup(self):
        self.driver = setupDriver()
        self.settingPage = SettingPage(self.driver)
        self.displayPage = DisplayPage(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    def test_serch(self):
        self.settingPage.display_click()
        self.displayPage.click_search()
        self.displayPage.input_text("hello")
        time.sleep(3)
        self.displayPage.click_back()