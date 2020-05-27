import time
from selenium.webdriver.common.by import By




class Login_page(BasePage):
    def __init__(self):
        super().__init__()
        self.username=(By.ID,"username")
        self.pwd=(By.ID,"password")
        self.verify=(By.ID,"verify_code")
        self.login_btn=(By.LINK_TEXT,"登    录")
    def find_username(self):
        return self.find_element(self.username)
    def find_pwd(self):
        return self.find_element(self.pwd)
    def find_verify(self):
        return self.find_element(self.verify)
    def find_login_btn(self):
        return self.find_element(self.login_btn)

class Login_handle(BaseHandle):
    def __init__(self):
        self.page1=Login_page()

    def input_username(self,name):
        self.input_text(self.page1.find_username(),name)

    def input_pwd(self,pwd):
        self.input_text(self.page1.find_pwd(),pwd)

    def input_verify(self,verify):
        self.input_text(self.page1.find_verify(),verify)

    def click_login_btn(self):
        self.page1.find_login_btn().click()

class Login_proxy():
    def __init__(self):
        self.handle=Login_handle()
        self.driver=DriverUnits.driver_setup()
    def login(self,name,pwd,verify):
        self.handle.input_username(name)
        self.handle.input_pwd(pwd)
        self.handle.input_verify(verify)
        self.handle.click_login_btn()
    def is_succeed(self):
        time.sleep(3)
        return self.driver.title