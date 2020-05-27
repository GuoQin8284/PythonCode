import time
from selenium import webdriver
import unittest
from parameterized import parameterized
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

"""
    要求：
        1. 采用UnitTest管理测试脚本，并生成测试报告
        2. 分成登录和新增收货地址两个用例
        3. 每执行一个操作暂停2秒，方便观看效果
        4. 在浏览器窗口最大化的状态下操作，设置隐式等待为30秒
        5. 在代码正常运行的情况下，实现测试数据的参数化
"""

def data_list():
    return [('苏格拉底', '上海市', '市辖区', '浦东新区', '三林镇', '山西省运城市芮城县', '044600', '13820599020')]

# 定义测试类
class TestLogin(unittest.TestCase):

    # 初始化操作方法封装--1.实例化浏览器驱动对象--2.隐式等待--3.打开页面
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)
        cls.driver.get('http://localhost/')

    # 释放资源，销毁的操作  1.退出浏览器驱动操作
    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.quit()

    # 定义测试方法
    # data_list = [('17634021383', 'Aa123456', '8888')]

    @parameterized.expand([('17634021383', 'Aa123456', '8888')])
    def test_1(self, userName, pwd, code):
        # 首页点击登录，进入登录页
        self.driver.find_element_by_link_text('登录').click()
        # 2. 输入用户名、密码和万能验证码，点击登录按钮登录系统
        self.driver.find_element_by_id('username').send_keys(userName)
        self.driver.find_element_by_id('password').send_keys(pwd)
        self.driver.find_element_by_name('verify_code').send_keys(code)

        # 点击登录按钮
        self.driver.find_element_by_css_selector('.J-login-submit').click()

    @parameterized.expand(data_list)
    def test_2(self, consignee, province, city, district, twon, address, zipcode, mobile):
        # 重新打开首页
        # self.driver.get('http://www.susr.com/')
        self.driver.find_element_by_xpath("//a[text()='首页']").click()
        # 1.点击我的订单
        self.driver.find_element_by_link_text('我的订单').click()

        # 2.选择‘账户设置’下的‘收货地址’选项
        # 切换新窗口
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # 实例化动作链的对象 ---perform()执行鼠标操作
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath('//span[text()="账户设置"]')).perform()
        # 鼠标悬停点击收货地址
        self.driver.find_element_by_link_text('收货地址').click()

        # 3.点击地址管理下的‘增加新地址’按钮
        self.driver.find_element_by_xpath('//span[text()="增加新地址"]').click()
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name('iframe'))

        # 4.输入地址信息，收货地址选择‘上海市-市辖区-浦东新区-三林镇’

        self.driver.find_element_by_name('consignee').send_keys(consignee)

        # 收货地址
        Select(self.driver.find_element_by_css_selector('#province')).select_by_visible_text(province)
        Select(self.driver.find_element_by_css_selector('#city')).select_by_visible_text(city)
        Select(self.driver.find_element_by_css_selector('#district')).select_by_visible_text(district)
        Select(self.driver.find_element_by_css_selector('#twon')).select_by_visible_text(twon)

        # 详细地址
        self.driver.find_element_by_css_selector('#address').send_keys(address)

        # 邮编

        self.driver.find_element_by_css_selector('.wi80-BFB').send_keys(zipcode)
        # 手机号
        self.driver.find_element_by_name('mobile').send_keys(mobile)
        # 5.其他选项任意输入
        # 6.点击‘保存收货地址’按钮

        self.driver.find_element_by_xpath('//*[text()="保存收货地址"]').click()
        # 7.关闭当前窗口
        self.driver.close()