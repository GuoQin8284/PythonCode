from selenium.webdriver.common.by import By

from new3.base import Base_page, Base_handle
from new3.unit_test import DriverUnit


class Page(Base_page):
    def __init__(self):
        super().__init__()
        self.name=(By.ID,"username")
        self.pwd=(By.ID,"password")
        self.verify_code=(By.ID,"verify_code")
        self.login_btn=(By.NAME,"sbtbutton")
    def dw_name(self):
        return self.find_element(self.name)
    def dw_pwd(self):
        return self.find_element(self.pwd)
    def dw_verify(self):
        return self.find_element(self.verify_code)
    def dw_btn_login(self):
        return self.find_element(self.login_btn)


class Handle(Base_handle):
    def __init__(self):
        self.dri=Page()
    def sr_name(self,name):
        self.input_text(self.dri.dw_name(),name)

    def sr_pwd(self, pwd):
        self.input_text(self.dri.dw_pwd(), pwd)

    def sr_verify(self, verify):
        self.input_text(self.dri.dw_verify(),verify)

    def sr_click(self):
        self.dri.dw_btn_login().click()

class Login():
    def __init__(self):
        self.sr_input=Handle()
    def shuru(self,name,pwd,verify):
        self.sr_input.sr_name(name)
        self.sr_input.sr_pwd(pwd)
        self.sr_input.sr_verify(verify)
        self.sr_input.sr_click()