from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


# 对象库层
class GoodsSearchPage(BasePage):
    # init方法
    def __init__(self):
        # 调用父类init方法,实例化浏览器驱动对象
        # 页面元素定位信息
        super().__init__()
        self.spname=(By.XPATH,"//div[@class='shop_name2']/a[contains(text(),'{}')]")
    # 定位商品名超链接 -- 参数--商品名关键字
    def find_goods_item(self, name):
        location=self.spname[0],self.spname[1].format(name)
        return self.find_element(location)


# 操作层
class GoodsSearchHandle(BaseHandle):
    # init方法
    def __init__(self):
        # 获取对象库层对象
        self.page=GoodsSearchPage()

    # 点击商品名超链接--参数-商品名关键字
    def click_goods_name(self, kw):
        self.page.find_goods_item(kw).click()


# 业务层
class GoodsSearchProxy:

    # init方法
    def __init__(self):
        # 获取操作层对象
        self.handle=GoodsSearchHandle()

    # 进入指定商品详情页--参数-商品名关键字
    def to_goods_detail_page(self, kw):
        # 点击指定商品
        self.handle.click_goods_name(kw)
