from selenium.webdriver.support.wait import WebDriverWait


class Action():

    def __init__(self,driver):
        self.driver=driver

    def find_element(self,reafure,timeout=10,poll=0.5):

        return WebDriverWait(self.driver,timeout,poll).until(lambda x: x.find_element(reafure[0],reafure[1]))

    def click(self,reafure):
        self.find_element(reafure).click()

    def input(self,reafure,content):
        self.find_element(reafure).send_keys(content)