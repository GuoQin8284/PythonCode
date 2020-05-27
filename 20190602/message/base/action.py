from selenium.webdriver.support.wait import WebDriverWait


class BaseAction():

    def __init__(self,driver):
        self.driver=driver

    def find_element(self,element,timeout=10,poll=0.5):
        # return self.driver.find_element(element[0],element[1])
        a = WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(element[0],element[1]))
        return a

    def click(self,feature):
        self.find_element(feature).click()

    def input(self,feature,content):
        self.find_element(feature).send_keys(content)
