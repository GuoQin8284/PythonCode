import time

import pytest

from base.setup_config import SetupConfig
from page.page import Page


class TestContact():

    def setup(self):
        self.driver=SetupConfig().init_driver()
        self.page=Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()
    @pytest.mark.parametrize(("name","content"),[("zhangsan","18012345678"),("lisi","13456781234")])
    def test_contact(self,name,content):
        self.page.page_add_contact.injoin_contact()
        self.page.page_add_contact.send_PhoneName(name)
        self.page.page_add_contact.send_PhoneNum(content)