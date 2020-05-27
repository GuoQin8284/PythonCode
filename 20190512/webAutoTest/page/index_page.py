from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


# 对象库层
from page.login_page import LoginProxy


class IndexPage(BasePage):
    # init方法
    def __init__(self):
        # 调用父类init方法,实例化浏览器驱动对象
        # 页面元素定位信息
        super().__init__()
        self.login=(By.LINK_TEXT,"登录")
        self.search=(By.ID,"q")
        self.search_button=(By.CLASS_NAME,"search_usercenter_btn")
    # 定位登录超链接
    def find_login_link(self):
        return self.find_element(self.login)

    # 定位搜索输入框
    def find_search_input(self):
        return self.find_element(self.search)

    # 定位搜索按钮
    def find_search_btn(self):
        return self.find_element(self.search_button)


# 操作层
class IndexHandle(BaseHandle):
    # init方法
    def __init__(self):
        # 获取对象库层对象
        self.driver=IndexPage()

    # 点击登录超链接
    def click_login_link(self):
        self.driver.find_login_link().click()

    # 输入框搜索 -- 参数-搜索关键字
    def input_search_text(self, kw):
        self.driver.find_search_input().send_keys(kw)
    # 点击搜索按钮
    def click_search_btn(self):
        self.driver.find_search_btn().click()


# 业务层
class IndexProxy:
    # init方法
    def __init__(self):
        # 获取操作层对象
        self.proxy=IndexHandle()
        self.login_proxy=LoginProxy()
    # 点击登录前往登录页
    def to_login_page(self):
        # 点击登录超链接
        self.proxy.click_login_link()

    # 搜索商品
    def search_goods(self, name):
        # 输入关键字
        self.proxy.input_search_text(name)
        # 点击搜索按钮
        self.proxy.click_search_btn()
