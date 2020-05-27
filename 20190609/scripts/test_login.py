from base.driver_base import init_driver
from page.me import Me


class TestLogin():

    def setup(self):
        self.driver=init_driver()
        self.me=Me(self.driver)
    def test_login(self):
        pass