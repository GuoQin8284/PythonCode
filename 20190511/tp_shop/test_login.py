import json
import unittest

import time
from parameterized import parameterized

from tp_shop.page_test import Proxy_driver
from tp_shop.unit_test import UnitDriver

def data_dump():
    data_1=[]
    with open("./data.json","r",encoding="utf-8") as f:
        test_data=json.load(f)
        print(test_data)
        for a in test_data:
            print("a",a)
            data_1.append((a.get("user"),
                          a.get("pwd"),
                          a.get("verify"),
                          a.get("bool"),
                          a.get("expect"),
                          ))
    print("data_1:",data_1)
    return data_1
class Test_driver(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=UnitDriver().setup()
        cls.page=Proxy_driver()

    @classmethod
    def tearDownClass(cls):
        UnitDriver.quit()

    def setUp(self):
        self.driver.get("http://localhost")
        self.driver.find_element_by_link_text("登录").click()

    @parameterized.expand(data_dump)
    def test_01(self,num,pwd,verify,bool,expect):
        self.page.proxy_login(num,pwd,verify)
        self.assertIn(expect,self.page.proxu_result(bool))