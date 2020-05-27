from selenium.webdriver.support.wait import WebDriverWait


class BaseAction():
    def __init__(self,driver):
        self.driver=driver

    def find_element(self,feature,timeout=10,poll=0.5):
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(feature[0],feature[1]))

    def click(self,feature):
        self.find_element(feature).click()

    def input(self,feature,content):
        self.find_element(feature).send_keys(content)
