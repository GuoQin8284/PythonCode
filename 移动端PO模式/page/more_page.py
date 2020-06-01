from selenium.webdriver.common.by import By

from base.action import Action


class MorePage(Action):
    mobile_network_button = By.XPATH, "//*[@text='移动网络']"

    def mobile_network_click(self):
        self.click(self.mobile_network_button)