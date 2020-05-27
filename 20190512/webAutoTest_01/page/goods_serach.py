from selenium.webdriver.common.by import By

from base.base_test import Base_page, Base_handle
from tools.utils import DriverUnit


class Page_goods(Base_page):

    def __init__(self):
        super().__init__()
        self.serach=(By.ID,"q")
        self.btn=(By.CLASS_NAME,"ecsc-search-button")

    def find_serach(self):
        return self.find_element(self.serach)

    def find_btn(self):
        return self.find_element(self.btn)


class Handle_goods(Base_handle):

    def __init__(self):
        self.page=Page_goods()

    def input_search(self,name):
        self.input_text(self.page.find_serach(),name)

    def click_btn(self):
        self.page.find_btn().click()


class Proxy_goods():
    def __init__(self):
        self.handle=Handle_goods()

    def search_goods(self,name):
        self.handle.input_search(name)
        self.handle.click_btn()