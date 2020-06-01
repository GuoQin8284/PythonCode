from selenium.webdriver.support.wait import WebDriverWait


class Action():
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature):
        feature_by, feature_value = feature
        ele = WebDriverWait(driver=self.driver, timeout=10, poll_frequency=0.5).\
            until(lambda x: x.find_element(feature_by, feature_value))
        return ele

    def click(self, feature):
        self.find_element(feature).click()

    def input(self, feature, text):
        self.find_element(feature).send_keys(text)