import time
from selenium.webdriver.common.by import By

from unit_add import DriverUnit


class Test_page():

    def __init__(self):
        self.driver=DriverUnit().setup()
        self.page_num=(By.ID,"simple{}")
        self.page_add=(By.ID,"simpleAdd")
        self.page_eq=(By.ID,"simpleEqual")
        self.page_result=(By.ID,"resultIpt")

    def input_num(self,location):
        location=(self.page_num[0],self.page_num[1].format(location))
        return self.driver.find_element(location[0],location[1])

    def input_add(self):
        return self.driver.find_element(*self.page_add)

    def input_eq(self):
        return self.driver.find_element(*self.page_eq)

    def input_result(self):
        return self.driver.find_element(*self.page_result)


class Test_handle():

    def __init__(self):
        self.handle_driver=Test_page()

    def click_num(self,num):
        self.handle_driver.input_num(num).click()

    def click_add(self):
        self.handle_driver.input_add().click()

    def click_eq(self):
        self.handle_driver.input_eq().click()

    def click_result(self):
        return self.handle_driver.input_result().get_attribute("value")

    def click_more_num(self,num):
        for n in str(num):
            print("for:",n)
            print("type:",type(n))
            self.click_num(str(n))


class Test_proxy():

    def __init__(self):
        self.driver=Test_handle()

    def proxy_num(self,x,y):
        self.driver.click_more_num(str(x))
        time.sleep(1)
        self.driver.click_add()
        time.sleep(1)
        self.driver.click_more_num(str(y))
        time.sleep(1)
        self.driver.click_eq()

    def proxy_result(self):
        return self.driver.click_result()