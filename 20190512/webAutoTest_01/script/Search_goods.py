import unittest

from page.goods_serach import Proxy_goods
from tools.utils import DriverUnit


class Search_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=DriverUnit.setup_driver()
        cls.search=Proxy_goods()

    @classmethod
    def tearDownClass(cls):
        DriverUnit.set_quit_driver(False)
        DriverUnit.quit_driver()

    def setUp(self):
        self.driver.get("http://localhost")
        # self.driver.find_element_by_link_text("登录").click()

    def test_search(self):
        self.search.search_goods("小米")