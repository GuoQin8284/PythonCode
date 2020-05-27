import unittest

from page.goods_detail_page import Detail_proxy
from tools.utils import DriverUnit


class Test_cart(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=DriverUnit.setup_driver()
        cls.page=Detail_proxy()

    @classmethod
    def tearDownClass(cls):
        DriverUnit.quit_driver()

    def test_01(self):
        self.page.join_cart("小米手机5")
        print("是否添加成功：",self.page.is_succeed("添加成功"))