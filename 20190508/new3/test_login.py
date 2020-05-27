import json
import unittest

import time

from parameterized import parameterized

from new3.Login_page import Login
from new3.unit_test import DriverUnit


def login_data():
    data_list = []
    with open("./data.json", "r", encoding="utf-8") as f:
        json_data = json.load(f)
        for data in json_data.values():
            data_list.append((data.get("username"),
                              data.get("pwd"),
                              data.get("verify_code"),
                              data.get("bool"),
                              data.get("expect")))
        print(data_list)
        return data_list

class Test_login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._driver=DriverUnit().unit_setup()

    @classmethod
    def tearDownClass(cls):
        DriverUnit.unit_quit()

    def setUp(self):
        self._driver.get("http://localhost")
        self._driver.find_element_by_link_text("登录").click()

    def tearDown(self):
        pass



    @parameterized.expand(login_data())
    def test_01(self,name,pwd,verfiy,bool,expect):
        self.login = Login()
        self.login.shuru(name,pwd,verfiy)
        time.sleep(3)
        if bool:
            title1=self._driver.title
            self.assertIn(expect,title1)
        else:
            msg=self._driver.find_element_by_xpath("//*[@id='layui-layer1']/div[2]").text
            self.assertIn(expect,msg)
