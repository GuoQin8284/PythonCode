from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


# 对象库层
from utils import DriverUtil


class GoodsDetailPage(BasePage):
    # init方法
    def __init__(self):
        super().__init__()
        # 调用父类init方法,实例化浏览器驱动对象
        # 业务元素定位信息
        self.join_cart=(By.ID,"join_cart")
        self.join_result=(By.XPATH,"//div[@class='conect-title']/span")

    # 定位加入购物车超链接
    def find_join_cart(self):
        return self.find_element(self.join_cart)

    # 定位加入结果提示信息
    def find_join_result(self):
        return self.find_element(self.join_result)


# 操作层
class GoodsDetailHandle(BaseHandle):
    # init方法
    def __init__(self):
        # 获取对象库层对象
        self.page=GoodsDetailPage()
    # 点击加入购物车超链接
    def click_join_cart(self):
        self.page.find_join_cart().click()
        self.driver=DriverUtil.get_driver()
    # 获取加入结果提示信息文本--返回文本信息
    def get_join_result(self):
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//div[@class='layui-layer-content']/iframe"))
        text=self.page.find_join_result().text
        return text
# 业务层
class GoodsDetailProxy:
    # init方法
    def __init__(self):
        # 获取操作层对象
        self.handle=GoodsDetailHandle()


    # 添加商品到购物车
    def join_goods_to_cart(self):
        self.handle.click_join_cart()

    # 判断是否加入成功 -- 返回是否成功布尔值
    def is_join_cart_success(self, expect):
        text=self.handle.get_join_result()
        return expect==text
