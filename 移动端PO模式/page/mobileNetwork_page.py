from selenium.webdriver.common.by import By

from base.action import Action


class MobileNetworkPage(Action):
    first_network_button = By.XPATH, "//*[@text='首选网络类型']"
    network_2G_button = By.XPATH, "//*[@text='2G']"
    network_3G_button = By.XPATH, "//*[@text='3G']"

    def first_network(self):
        self.click(self.first_network_button)

    def network_2G(self):
        self.click(self.network_2G_button)

    def network_3G(self):
        self.click(self.network_3G_button)