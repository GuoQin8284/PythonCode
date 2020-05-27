import unittest

from page.adviser.login_page import loginProxy


class Login(unittest.TestCase):

    def test_01(self):
        url="https://adviser.osid.org.cn/"
        self.login=loginProxy(url)
        self.login.login('15549080517','Aa1234')