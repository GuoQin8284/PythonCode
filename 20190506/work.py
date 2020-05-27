# 1.
# 打开TPshop网站首页，完成以下操作：
import time
import unittest

from parameterized.parameterized import parameterized
from selenium import webdriver
from selenium.webdriver.common import alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


class Test_unit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("http://localhost")
        # url = cls.driver.current_url
        # try:
        #     cls.assertEqual("http://localhost",url)
        # except Exception as e:
        #     print(e)
        #     raise e
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
# 用例一:
# 1.
# 点击‘登录’跳转到登录页面
    def test_01(self):
        print("1")
        self.driver.find_element_by_link_text("登录").click()

# 2.
# 输入用户名、密码和万能验证码，点击登录按钮登录系统
        self.driver.find_element_by_id("username").send_keys("18012345678")
        self.driver.find_element_by_id("password").send_keys("123456")
        self.driver.find_element_by_id("verify_code").send_keys("8888")
        self.driver.find_element_by_xpath("//a[@class='J-login-submit']").click()
        try:
            self.assertNotEqual("http://localhost/Home/User/index.html",self.driver.current_url)
        except Exception as e:
            print("登录失败")
            raise e
# 用例二:
# 3.
# 重新打开首页，点击‘我的订单’进入后台管理页面
    def test_02(self):
        print("2")
        self.driver.find_element_by_xpath("//a[@href='/Home/Index/index.html']").click()
        self.driver.find_element_by_xpath("//a[@href='/Home/Order/order_list.html']").click()
# 4.
# 选择‘账户设置’下的‘收货地址’选项
        self.driver.switch_to.window(self.driver.window_handles[-1])
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath("//div[@class='u-dt']/span")).perform()
        self.driver.find_element_by_xpath("//a[@href='/Home/User/address_list.html']").click()
# 5.
# 点击地址管理下的‘增加新地址’按钮
        first_text = self.driver.find_element_by_xpath("//p[@class='gp_num2']/em[1]").text
        self.driver.find_element_by_xpath("//span[text()='增加新地址']").click()
# 6.
# 输入地址信息，收货地址选择‘上海市 - 市辖区 - 浦东新区 - 三林镇’，其他选项任意输入
        self.driver.switch_to.frame("layui-layer-iframe100001")
    # address = [("铁蛋"), ("上海市"), ("市辖区"), ("浦东新区"), ("三林镇"), ("黄浦江"), (18012345678)]
        self.driver.find_element_by_css_selector("input[class='wi80-BFB'").send_keys("铁蛋")
        Select(self.driver.find_element_by_id("province")).select_by_visible_text("上海市")
        Select(self.driver.find_element_by_id("city")).select_by_visible_text("市辖区")
        Select(self.driver.find_element_by_id("district")).select_by_visible_text("浦东新区")
        Select(self.driver.find_element_by_id("twon")).select_by_visible_text("三林镇")
        self.driver.find_element_by_id("address").send_keys("黄浦江")
        # self.driver.find_element_by_xpath("//input[@class='wi40-BFB' and @name='mobile']").send_keys("18012345678")
        # 7.
        # 点击‘保存收货地址’按钮
        self.driver.get_screenshot_as_file("./img/img{}.png".format(time.strftime("%Y%m%d%H%M%S")))
        self.driver.find_element_by_xpath("//span[text()='保存收货地址']").click()
        time.sleep(2)
        # self.driver.get_screenshot_as_file("./img/img{}.png".format(time.strftime("%Y%m%d%H%M%S")))

        try:
            secend_text = self.driver.find_element_by_xpath("//p[@class='gp_num2']/em[1]").text
            print("添加成功")
            self.assertNotEqual(first_text,secend_text)
        except Exception as e:
            print("e:",e)
            b = self.driver.switch_to.alert.text
            print("alert",b)
            time.sleep(3)
            self.driver.get_screenshot_as_file("./img/img{}.png".format(time.strftime("%Y%m%d%H%M%S")))
            time.sleep(3)
            # raise e
# 8.
# 关闭当前窗口

# 要求：
# 1.
# 采用UnitTest管理测试脚本，并生成测试报告
# 2.
# 分成登录和新增收货地址两个用例
# 3.
# 每执行一个操作暂停2秒，方便观看效果
# 4.
# 在浏览器窗口最大化的状态下操作，设置隐式等待为30秒
# 5.
# 在代码正常运行的情况下，实现测试数据的参数