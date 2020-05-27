import unittest

from v3_2 import Driver
from v4 import login_proxy


class Deng_lu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=Driver()
        cls.driver.driver_setup()
        cls.denglu=login_proxy()
    @classmethod
    def tearDownClass(cls):
        cls.driver.driver_quit()

    def setUp(self):
        self
        self.driver.driver_setup().find_element_by_link_text("登录").click()
    def test01(self):
        self.denglu.login("18000000000","123456","8888")
    def test02(self):
        self.denglu.login("18012345678","123321","8888")