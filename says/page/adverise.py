from selenium.webdriver.common.by import By

from driver.action import Action
import logging


class AdviserPage(Action):
    def __init__(self,driver):
        super().__init__(driver)
        self.loginName=(By.XPATH,"//input[@name='username']")
        self.loginPwd=(By.XPATH,"//input[@name='password']")
        self.login=(By.LINK_TEXT,"登录")

    def ele_loginName(self):
        logging.debug("")
        return self.find_element(self.loginName)
    def ele_loginPwd(self):
        logging.debug("")
        return self.find_element(self.loginPwd)
    def ele_login(self):
        logging.debug("")
        return self.find_element(self.login)

class AdviserHandle(AdviserPage):
    logging.debug("")
    def click_loginName(self,name):
        self.ele_loginName().send_keys(name)
    def click_loginPwd(self,pwd):
        self.ele_loginPwd().send_keys(pwd)
    def click_login(self):
        self.ele_login().click()

class AdveriseProxy(AdviserHandle):
    def login(self,name,pwd):
        print("name=,pwd=")
        logging.debug("name={},pwd={}".format(name,pwd))
        self.click_loginName(name)
        self.click_loginPwd(pwd)
        self.click_login()
