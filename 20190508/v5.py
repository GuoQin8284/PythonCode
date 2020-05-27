from selenium.webdriver.common.by import By

from utils import DriverUtil


class LoginPage1():
    # 获取浏览器驱动对象
    def __init__(self):
        self.driver = DriverUtil.get_driver()
        self.uesrname = (By.ID,"username")
        self.password = (By.ID,"password")
        self.verify = (By.ID,"verify_code")
        self.login_btn = (By.NAME,"sbtbutton")
    # 元素定位方法
    def find_username(self):
        return self.driver.find_element(self.uesrname[0],self.uesrname[1])
    def find_password(self):
        return self.driver.find_element(self.password[0], self.password[1])
    def find_verify(self):
        return self.driver.find_element(self.verify[0], self.verify[1])
    def find_login_btn(self):
        return self.driver.find_element(self.login_btn[0], self.login_btn[1])


class LoginHandle():

    def __init__(self):
        self.login=LoginPage1()

    def input_username(self,username):
        self.login.find_username().clear()
        self.login.find_username().send_keys(username)

    def input_password(self,password):
        self.login.find_password().clear()
        self.login.find_password().send_keys(password)

    def input_verify(self,verify):
        self.login.find_verify().clear()
        self.login.find_verify().send_keys(verify)

    def click_login_btn(self):
        self.login.find_login_btn().click()


class login_proxy():

    def __init__(self):
        self.login_handle = LoginHandle()

    def login(self,username,password,verify):
        self.login_handle.input_username(username)
        self.login_handle.input_password(password)
        self.login_handle.input_verify(verify)
        self.login_handle.click_login_btn()