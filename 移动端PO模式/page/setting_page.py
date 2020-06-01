from selenium.webdriver.common.by import By

from base.action import Action


class SettingPage(Action):
    display_button = By.XPATH, "//*[@text='显示']"
    more_button = By.XPATH, "//*[@text='更多']"

    def display_click(self):
        self.click(self.display_button)

    def more_click(self):
        self.click(self.more_button)