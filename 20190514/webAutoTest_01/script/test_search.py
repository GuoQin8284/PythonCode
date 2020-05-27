import logging
import unittest

from parameterized.parameterized import parameterized

from page.search_page import Search_proxy
from units import DriverUnits, test_case_json


def test_data():
    test_list=[]
    json_data = test_case_json()
    test_case=json_data.get("goods")
    for case in test_case:
        test_list.append((case.get("goods")))
    return test_list

class Test_search(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=DriverUnits.driver_setup()
        cls.page=Search_proxy()
    @classmethod
    def tearDownClass(cls):
        DriverUnits.driver_quit()
    def setUp(self):
        self.driver.get("http://localhost")
    @parameterized.expand(test_data)
    def test_search_box(self,goods):
        self.page.search_goods(goods)
        logging.info(goods)