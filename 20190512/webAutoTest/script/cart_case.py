# 参数化,数据驱动
# 创建测试类
import time
import unittest

from page.goods_detail_page import GoodsDetailProxy
from page.goods_search_page import GoodsSearchProxy
from page.index_page import IndexProxy
from page.login_page import LoginProxy
from utils import DriverUtil


class TestCart(unittest.TestCase):

    # fixture
    @classmethod
    def setUpClass(cls):
        cls.driver=DriverUtil.get_driver()
        cls.search_proxy=GoodsSearchProxy()
        cls.detail_proxy=GoodsDetailProxy()
        cls.index_proxy=IndexProxy()
        cls.login_proxy = LoginProxy()
        cls.detail_proxy=GoodsDetailProxy()

    @classmethod
    def tearDownClass(cls):
        DriverUtil.quit_driver()

        # 打开首页
    def setUp(self):
        self.driver.get("http://localhost")
        self.driver.find_element_by_link_text("登录").click()


    # 创建测试方法,断言
    def test_cart(self):
        # self.index_proxy.to_login_page()
        self.login_proxy.login("18012345678","123456","8888")
        self.index_proxy.search_goods("小米")
        self.search_proxy.to_goods_detail_page("小米")
        self.detail_proxy.join_goods_to_cart()
        a = self.detail_proxy.is_join_cart_success("添加成功")
        print(a)
        # 注意点 -- 如果定位失败了怎么排查问题

# 参数化,数据驱动
