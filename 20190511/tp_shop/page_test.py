import time
from selenium.webdriver.common.by import By

from tp_shop.base_test import Base_page, Base_handle
from tp_shop.unit_test import UnitDriver


class Page_driver(Base_page):

    def __init__(self):
        super().__init__()
        self.username=(By.ID,"username")
        self.password=(By.ID,"password")
        self.verify_code=(By.ID,"verify_code")
        self.login_btn=(By.NAME,"sbtbutton")

    def find_username(self):
        return self.base_page(self.username)

    def find_password(self):
        return self.base_page(self.password)

    def find_verify_code(self):
        return self.base_page(self.verify_code)

    def find_login(self):
        return self.base_page(self.login_btn)


class Handle_driver(Base_handle):
    def __init__(self):
        self.dri=Page_driver()

    def input_username(self,num):
        self.base_handle(self.dri.find_username(),num)

    def input_password(self,pwd):
        self.base_handle(self.dri.find_password(), pwd)

    def input_verify(self,verify):
        self.base_handle(self.dri.find_verify_code(), verify)

    def click_login(self):
        self.dri.find_login().click()


class Proxy_driver():

    def __init__(self):
        self.driver=Handle_driver()
        self.udriver=UnitDriver.setup()

    def proxy_login(self,num,pwd,verify):
        self.driver.input_username(num)
        self.driver.input_password(pwd)
        self.driver.input_verify(verify)
        self.driver.click_login()

    def proxu_result(self,bool):
        if bool is True:
            time.sleep(3)
            msg = self.udriver.title
            print("true_msg:",msg)
            self.udriver.find_element_by_xpath('//a[@title="退出"]').click()
            return msg
        else:
            time.sleep(3)
            msg = self.udriver.find_element_by_xpath('//*[@id="layui-layer1"]/div[2]').text
            print("msg:",msg)
            return msg
