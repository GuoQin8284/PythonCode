import time

import pytest

from base.analusis import analyze_file
from base.setup_driver import SetupDriver
from page.page import Page


class SendMessage():

    def setup(self):
        self.driver=SetupDriver().init_driver()
        self.page=Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    @pytest.mark.parametrize(("*args"),analyze_file("data.yaml","test_send_message"))
    def test_send_message(self,args):
        PhoneNum=args["phone"]
        content = args["content"]
        self.page.message.click_NewMessage()
        self.page.message.input_ReceiveNum_btn(PhoneNum)
        self.page.message.input_content(content)
        self.page.message.send_message()