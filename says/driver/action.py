import logging

class Action():
    def __init__(self,driver):
        self.driver=driver
        logging.debug(self.driver)

    def find_element(self,ele):
        logging.debug("")
        return self.driver.find_element(ele[0],ele[1])

    # def click_ele(self,ele):
    #     self.find_element(ele).click()
    #
    # def send_keys(self,ele,content):
    #     self.find_element(ele).semd_keys(content)
