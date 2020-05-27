import json
import unittest

import time
from parameterized import parameterized

from page.login_page import Proxy_page
from tools.utils import DriverUnit

def data():
    data_list=[]
    with open("../data/login.json","r",encoding="utf-8") as f:
        i = json.load(f)
        for a in i:
            data_list.append((a.get("username"),
                             a.get("pwd"),
                             a.get("verify")))
        return data_list

class Test_login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dirver=DriverUnit.setup_driver()
        cls.page=Proxy_page()
        # DriverUnit.set_quit_driver(False)

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        DriverUnit.quit_driver()

    def setUp(self):
        self.dirver.get("http://localhost")
        self.dirver.find_element_by_link_text("登录").click()

    @parameterized.expand(data())
    def test_login(self,name,pwd,verfiy):
        self.page.login(name,pwd,verfiy)

    @parameterized.expand(data())
    def test_login(self):
        self.page.login("18012345678","123456","8888")