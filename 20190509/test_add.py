import unittest

from parameterized import parameterized

from page_add import Test_proxy
from unit_add import DriverUnit


class Test_add(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=DriverUnit().setup()
        cls.page_01=Test_proxy()

    @classmethod
    def tearDownClass(cls):
        DriverUnit().quit()

    @parameterized.expand([(1,2,3)])
    def test_add(self,num1,num2,expect):
        print("num1:",num1)
        print("num2:", num2)
        print("expect:", expect)
        self.page_01.proxy_num(num1,num2)
        a = self.page_01.proxy_result()
        print("result:",a)
        self.assertEqual(str(expect),a)
