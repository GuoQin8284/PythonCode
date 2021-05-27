import logging
import unittest

from parameterized import parameterized

from api.login import Login
from tools.analysis import analysis_data


class Test_Login(unittest.TestCase):


    def setUp(self) -> None:
        self.login = Login()


    @parameterized.expand(analysis_data("login_data.json"))
    def test_login(self,res_data):
        response = self.login.login(res_data)
        text = response.text
        status_code = response.status_code
        expect = res_data["expect"]
        logging.info("expect: "+expect)
        logging.info("接口返回的text: "+text)
        logging.info("状态码："+ str(status_code))
        self.assertIn(expect, response.text)
        self.assertEqual(200, response.status_code)