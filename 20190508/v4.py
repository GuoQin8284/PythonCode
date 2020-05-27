from utils import DriverUtil


class LoginPage1():
    # 获取浏览器驱动对象
    def __init__(self):
        self.driver = DriverUtil.get_driver()
        self.uesrname = None
        self.password = None
        self.verify = None
        self.login_btn = None
    # 元素定位方法
    def find_username(self):
        return self.driver.find_element_by_id("username")
    def find_password(self):
        return self.driver.find_element_by_id("password")
    def find_verify(self):
        return self.driver.find_element_by_id("verify_code")
    def find_login_btn(self):
        return self.driver.find_element_by_name("sbtbutton")


class LoginHandle():

    def __init__(self):
        self.login=LoginPage1()

    def input_username(self,username):
        self.login.find_username().send_keys(username)

    def input_password(self,password):
        self.login.find_password().send_keys(password)

    def input_verify(self,verify):
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