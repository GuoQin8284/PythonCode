import json
import logging
import unittest

from parameterized import parameterized

from config import json_file
from page.login_page import Login_proxy
from units import DriverUnits, test_case_json


def test_data():
    test_list=[]
    json_data = test_case_json()
    test_case=json_data.get("login")
    for case in test_case:
        test_list.append((case.get("username"),
                          case.get("pwd"),
                          case.get("verify"),
                          case.get("expect")))
    return test_list


class Test_login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=DriverUnits.driver_setup()
        cls.page=Login_proxy()
    @classmethod
    def tearDownClass(cls):
        DriverUnits.driver_quit()

    def setUp(self):
        self.driver.get("http://localhost")
        self.driver.find_element_by_link_text("登录").click()

    @parameterized.expand(test_data())
    def test_login01(self,name,pwd,code,expect):
        # print("name:{},pwd:{},code:{},expect:{}".format(name,pwd,code,expect))
        self.page.login(name,pwd,code)
        self.assertIn(expect,self.page.is_succeed())
        logging.info("name:{},pwd:{},code:{},expect:{}".format(name,pwd,code,expect))