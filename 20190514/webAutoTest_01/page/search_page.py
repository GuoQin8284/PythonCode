from selenium.webdriver.common.by import By
from base.base_page import BasePage
class Search_page(BasePage):
    def __init__(self):
        super().__init__()
        self.search_box=(By.ID,"q")
        self.search_btn=(By.CLASS_NAME,"ecsc-search-button")
    def find_box(self):
        return self.find_element(self.search_box)
    def find_btn(self):
        return self.find_element(self.search_btn)
class Search_handle():
    def __init__(self):
        self.page=Search_page()
    def input_box(self,goods):
        self.page.find_box().send_keys(goods)
    def click_btn(self):
        self.page.find_btn().click()
class Search_proxy():
    def __init__(self):
        self.handle=Search_handle()
    def search_goods(self,goods):
        self.handle.input_box(goods)
        self.handle.click_btn()