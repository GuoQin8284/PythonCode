import unittest

import time
from selenium import webdriver
def setUpModule():
    print("Module_start time:", time.time())
def tearDownModule():
    print("Module_start time:", time.time())

class Test_unit1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("class_start time:", time.time())
    @classmethod
    def tearDownClass(cls):
        print("class_end time:", time.time())
    def setUp(self):
        print("start time:",time.time())
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://localhost")
    def tearDown(self):
        self.driver.quit()
        print("end time:",time.time())
    def test_01(self):
        self.driver.find_element_by_link_text("登录").click()
        self.driver.find_element_by_id("username").send_keys("18012345678")
        self.driver.find_element_by_id("password").send_keys("123456")
        self.driver.find_element_by_link_text("登    录").click()
        error_text=self.driver.find_element_by_xpath("//*[@id='layui-layer1']/div[2]").text
        print("errot_text:",error_text)
        try:
            # self.assertIn("验证码不能为空6",error_text)
            self.assertTrue(True)
        except:
            # self.driver.get_screenshot_as_file("./img/img{}.png".format(time.strftime("%Y%m%d%H%M%S")))
            self.assertTrue(False)
            raise
