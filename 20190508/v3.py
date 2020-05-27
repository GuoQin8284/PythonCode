import unittest
import time

from selenium import webdriver


class Test_login(unittest.TestCase):
    error_type = ("密码错误!", "账号不存在!")
    driver=None
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(15)
    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.driver.quit()

    def setUp(self):
        self.driver.get("http://localhost")

    def tearDown(self):
        try:
            self.assertIn(self.a,self.error_type)
            print(self.a)
        except Exception as e:
            print("未知错误：", e)
            raise e
    def test01_zhanghao_error(self):
        self.driver.find_element_by_link_text("登录").click()
        self.driver.find_element_by_id("username").send_keys("13000000000")
        self.driver.find_element_by_id("password").send_keys("123456")
        self.driver.find_element_by_id("verify_code").send_keys("8888")
        self.driver.find_element_by_link_text("登    录").click()
        self.a = self.driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[2]').text

    def test02_password_error(self):
        self.driver.find_element_by_link_text("登录").click()
        self.driver.find_element_by_id("username").send_keys("18012345678")
        self.driver.find_element_by_id("password").send_keys("123321")
        self.driver.find_element_by_id("verify_code").send_keys("8888")
        self.driver.find_element_by_link_text("登    录").click()
        self.a=self.driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[2]').text