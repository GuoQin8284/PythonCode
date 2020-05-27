# 使用 unittest 管理测试用例
import time
import unittest

# 1.创建测试类
# from day6.utils import get_tips_msg, DriverUtil
# from day6.v4.login_page import LoginPage
from utils import DriverUtil
from v4 import LoginPage1


class TestLogin(unittest.TestCase):
    # 4.fixture -- class
    @classmethod
    def setUpClass(cls):
        # 打开浏览器
        # 获取驱动对象的工具类 -- 获取浏览器驱动
        cls.driver = DriverUtil.get_driver()

        # 获取对象库层对象
        cls.login_page = LoginPage1()

    @classmethod
    def tearDownClass(cls):
        # 关闭浏览器
        # 获取驱动对象的工具类 -- 退出浏览器驱动
        DriverUtil.quit_driver()

    # 4.fixture -- method
    def setUp(self):
        # 打开页面 -- 驱动调用get方法打开页面
        self.driver.get("http://localhost")
        # 点击首页的登陆链接
        self.driver.find_element_by_class_name('red').click()

    def tearDown(self):
        # 等待查看结果
        time.sleep(2)

    # 2.创建测试方法
    # 用户名不存在用例
    def test01_login_username_not_exist(self):
        # 业务操作 -- 元素定位和元素操作
        # 输入 用户名 密码  验证码
        self.login_page.find_username().send_keys("13112345678")
        self.login_page.find_pwd().send_keys("123456")
        self.login_page.find_verify_code().send_keys("8888")

        # 点击登陆按钮
        self.login_page.find_login_btn().click()

        # 登陆提示信息
        msg = get_tips_msg()

        # 3.断言assert
        self.assertIn("账号不存在", msg)

    # 密码错误用例
    def test02_login_password_error(self):
        # 业务操作 -- 元素定位和元素操作
        # 输入 用户名 密码  验证码
        self.login_page.find_username().send_keys("13012345678")
        self.login_page.find_pwd().send_keys("123123456")
        self.login_page.find_verify_code().send_keys("8888")

        # 点击登陆按钮
        self.login_page.find_login_btn().click()

        # 登陆提示信息
        # 使用工具模块中的获取弹出框的提示消息工具方法
        msg = get_tips_msg()

        # 3.断言assert
        self.assertIn("密码错误", msg)
