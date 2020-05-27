# 创建测试类

# 测试类
import unittest

import time

from page.index_page import IndexProxy
from page.login_page import LoginProxy
from utils import DriverUtil


class Test_login(unittest.TestCase):


    # fixture
    @classmethod
    def setUpClass(cls):
        # 获取浏览器驱动对象
        cls.driver = DriverUtil.get_driver()
        cls.login_proxy = LoginProxy()
        cls.indexproxy = IndexProxy()
        # 获取用例页面

    @classmethod
    def tearDownClass(cls):
        DriverUtil.quit_driver()

    def setUp(self):
        self.driver.get("http://localhost")
        self.driver.find_element_by_link_text("登录").click()


        # 打开首页
    def test_login(self):
        # 点击进入登录页
        self.login_proxy.login("18012345678", "123456", "8888")
        time.sleep(3)
    # 测试方法,断言
        title=self.driver.title
        self.assertIn("我的账户",title)
        # 登录
    def test_index(self):
        self.indexproxy.to_login_page()
        self.login_proxy.login("18012345678", "123456", "8888")
        time.sleep(3)
        title=self.driver.title
        self.assertIn("搜索列表",title)


# 参数化,数据驱动
