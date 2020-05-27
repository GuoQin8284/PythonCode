from selenium.webdriver.common.by import By

from base.base_test import Base_page, Base_handle
from tools.utils import DriverUnit


class Detail_page(Base_page):
    def __init__(self):
        super().__init__()
        self.goods=(By.XPATH,"//div[@class='shop_name2']/a[contains(text(),'{}')]")
        self.cart=(By.ID,"join_cart")
        self.get_frame=(By.XPATH,"//div[@class='layui-layer-content']/iframe")
        self.result=(By.XPATH,"//div[@class='conect-title']/span")

    def find_goods(self,name):
        location=(self.goods[0],self.goods[1].format(name))
        return self.find_element(location)

    def find_cart(self):
        return self.find_element(self.cart)

    def find_frame(self):
        return self.find_element(self.get_frame)

    def find_result(self):
        return self.find_element(self.result)


class Detail_handle(Base_handle):

    def __init__(self):
        self.page=Detail_page()
        self.driver=DriverUnit().setup_driver()
    def click_goods(self,name):
        self.page.find_goods(name).click()

    def click_cart(self):
        self.page.find_cart().click()

    def swich_frame(self):
        self.driver.switch_to.frame(self.page.find_frame())

    def get_result(self):
        return self.page.find_result().text

class Detail_proxy():

    def __init__(self):
        self.handle=Detail_handle()

    def join_cart(self,name):
        self.handle.click_goods(name)
        self.handle.click_cart()

    def is_succeed(self,expect):
        self.handle.swich_frame()
        # self.result=
        return expect==self.handle.get_result()