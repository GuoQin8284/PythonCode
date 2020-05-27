

# 登陆tools
import json
import unittest
import logging

import time
from parameterized.parameterized import parameterized
from selenium.webdriver.common.by import By

from driver.driver import Driver
from page.adverise import AdveriseProxy
from page.tools_says import Says_proxy


# def Login_name():
#     with open(file="../data/tools_login.json",mode="r",encoding="utf-8") as f :
#         data_list=[]
#         data=json.load(f)
#         data1=data.get("data")
#         data_list.append((data1.get("name"),
#                           data1.get("password")))
#         print("data_list=",data_list)
#         return data_list

class Test_ToolsLogin(unittest.TestCase):


    def setUp(self):
        logging.debug("")
        self.driver=Driver().driver()
        self.driver.get("https://adviser.osid.org.cn")
        # self.says=Says_proxy(self.driver)
        self.says_login=AdveriseProxy(self.driver)

    def tearDown(self):
        pass

    # @parameterized.expand(Login_name)
    # def test01_login_tools(self,name,pwd):
    #     print("name=",name)
    #     print("pwd=",pwd)
    #     self.driver.find_element_by_name("name").send_keys(name)
    #     self.driver.find_element_by_name("pwd").send_keys(pwd)
    #     self.driver.find_element_by_xpath("//*[@id='Duoyue']/div/div[1]/form/span").click()
    #     time.sleep(2)
        # self.driver.find_element(self.says1[0],self.says1[1]).click()
        # time.sleep(3)
        # self.says.says()
    def test01(self):
        name="15549080517"
        pwd="Aa1234"
        logging.debug("name={},pwd={}" .format (name, pwd))
        self.says_login.login(name,pwd)
        logging.debug("")