from selenium.webdriver.common.by import By

from base.base_test import Base_page, Base_handle


class Page_login(Base_page):
    def __init__(self):
        super().__init__()
        self.name=(By.ID,"username")
        self.pwd=(By.ID,"password")
        self.verify=(By.ID,"verify_code")
        self.login_btn=(By.XPATH,"//div[@class='login_bnt']/a")

    def find_username(self):
        return self.find_element(self.name)

    def find_password(self):
        return self.find_element(self.pwd)

    def find_verify_code(self):
        return self.find_element(self.verify)

    def find_login_btn(self):
        return self.find_element(self.login_btn)


class Handle_page(Base_handle):
    def __init__(self):
        self.page=Page_login()

    def input_username(self,name):
        self.input_text(self.page.find_username(),name)

    def input_password(self,pwd):
        self.input_text(self.page.find_password(),pwd)

    def input_verify_code(self,verify):
        self.input_text(self.page.find_verify_code(),verify)

    def click_login_btn(self):
        self.page.find_login_btn().click()


class Proxy_page():
    def __init__(self):
        self.handle=Handle_page()

    def login(self,name,pwd,verify):
        self.handle.input_username(name)
        self.handle.input_password(pwd)
        self.handle.input_verify_code(verify)
        self.handle.click_login_btn()
