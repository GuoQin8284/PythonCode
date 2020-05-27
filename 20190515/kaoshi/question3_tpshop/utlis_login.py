import unittest

import time
from selenium import webdriver


class Test_login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("http://localhost")

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

    def test_login(self):
        self.driver.find_element_by_link_text("登录").click()
        self.driver.find_element_by_id("username").send_keys("18012345678")
        self.driver.find_element_by_id("password").send_keys("123456")
        self.driver.find_element_by_id("verify_code").send_keys("8888")
        self.driver.find_element_by_link_text("登    录").click()
        time.sleep(3)
        text = self.driver.find_element_by_xpath("//div[@class='mu-midd fl']/a[@class='mu-m-phone']").text
        try:
            self.assertNotIn("admin",text)
            print(text)
            self.driver.get_screenshot_as_file("./scrren_shot/login_scrren{}.png".format(time.strftime("%Y%m%d%H%M%S")))

        except Exception as e:
            print("未知错误：",e)