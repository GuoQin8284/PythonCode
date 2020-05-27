from selenium.webdriver.common.by import By

from page.Base import Base_page, Base_handle


class LoginPage(Base_page):

    def __init__(self,url):
        print("url",url)
        super().__init__(url)

        self.loginName=(By.NAME,'username')
        self.loginPwd=(By.NAME,'password')
        self.loginBtn=(By.XPATH,'//*[@id="App"]/div/div[2]/div/div/section[2]/div/section/form/button')

    def ele_loginName(self):
        return self.find_element(self.loginName)

    def ele_loginPwd(self):
        return self.find_element(self.loginPwd)

    def ele_loginBtn(self):
        return self.find_element(self.loginBtn)

class LoginHandle(Base_handle):

    def __init__(self,url):
        self.loginPage=LoginPage(url)

    def inputName(self,name):
        self.Input_text(self.loginPage.ele_loginName(),name)

    def inputPwd(self,pwd):
        self.Input_text(self.loginPage.ele_loginPwd(),pwd)

    def clickLogin(self):
        self.Click(self.loginPage.ele_loginBtn())

class loginProxy():

    def __init__(self,url):
        self.loginhandle=LoginHandle(url)

    def login(self,name,pwd):
        self.loginhandle.inputName(name)
        self.loginhandle.inputPwd(pwd)
        self.loginhandle.clickLogin()