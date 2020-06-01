import time

from base.setup_driver import setupDriver
from page.mobileNetwork_page import MobileNetworkPage
from page.more_page import MorePage
from page.setting_page import SettingPage


class TestNetwork():

    def setup(self):
        self.driver = setupDriver()
        self.settingPage = SettingPage(self.driver)
        self.morePage = MorePage(self.driver)
        self.mobileNetworkPage = MobileNetworkPage(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    def test_2G(self):
        self.settingPage.more_click()
        self.morePage.mobile_network_click()
        self.mobileNetworkPage.first_network()
        self.mobileNetworkPage.network_2G()

    def test_3G(self):
        self.settingPage.more_click()
        self.morePage.mobile_network_click()
        self.mobileNetworkPage.first_network()
        self.mobileNetworkPage.network_3G()