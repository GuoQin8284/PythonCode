import unittest
from unittest import mock

#
def login(tel,verify_code):
    return False


class TestLogin(unittest.TestCase):

    def test_cart(self):
        login=mock.Mock(return_value=True)
        result = login("110","9999")
        print("登录结果",result)


