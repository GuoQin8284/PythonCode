import unittest

from v3_2 import Driver


class Test_login(unittest.TestCase):
    error_type = ("密码错误!", "账号不存在!")
    @classmethod
    def setUpClass(cls):
        cls.driver=Driver.driver_setup()
    @classmethod
    def tearDownClass(cls):
        cls.driver =Driver.driver_quit()

    def setUp(self):
        self.driver.get("http://localhost")
    def tearDown(self):
        try:
            self.assertIn(Driver.driver_text,self.error_type)
            print(Driver.driver_text)
        except Exception as e:
            print("未知错误：", e)
            raise e
    def test01_zhanghao_error(self):
        self.driver.find_element_by_link_text("登录").click()
        self.driver.find_element_by_id("username").send_keys("13000000000")
        self.driver.find_element_by_id("password").send_keys("123456")
        self.driver.find_element_by_id("verify_code").send_keys("8888")
        self.driver.find_element_by_link_text("登    录").click()
        a = Driver.driver_text
        print(a)

    def test02_password_error(self):
        self.driver.find_element_by_link_text("登录").click()
        self.driver.find_element_by_id("username").send_keys("18012345678")
        self.driver.find_element_by_id("password").send_keys("123321")
        self.driver.find_element_by_id("verify_code").send_keys("8888")
        self.driver.find_element_by_link_text("登    录").click()
        print(Driver.driver_text)