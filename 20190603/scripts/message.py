import time

import pytest

from base.analysis_data import data
from base.setup_driver import SetupDriver
from page.page import Page


class AddContact():

    def setup(self):
        self.driver=SetupDriver().InitDriver()
        self.page=Page(self.driver)
    def teartown(self):

        time.sleep(3)
        self.driver.quit()

    @pytest.mark.parametrize("args",data("data.yaml","message","test_add_message"))
    def test_add_message(self,args):
        name=args["name"]
        num=args["num"]
        print(name)
        print(num)
        self.page.contact.click_contact()
        self.page.contact.click_local_save()
        self.page.contact.input_name(name)
        self.page.contact.input_num(num)