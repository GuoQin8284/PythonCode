import time

from selenium import webdriver


# 定义获取驱动对象的工具类
class DriverUtil:
    # 定义一个类属性,专门用来保存浏览器驱动对象
    _driver = None

    # 为了调用方便,把这个方法定义为类方法--类名.方法名()

    # 问题 如何保证只有一个浏览器驱动对象呢?
    #     定义一个类属性,专门用来保存浏览器驱动对象
    #     如果类属性为空,则创建一个浏览器驱动对象,并返回
    #     如果类属性非空,则直接返回类属性中保存的浏览器驱动对象
    @classmethod
    def get_driver(cls):
        # 初始化一个浏览器驱动对象
        # 返回浏览器驱动对象

        # 如果类属性为空,则创建一个浏览器驱动对象,并返回
        # 如果类属性非空,则直接返回类属性中保存的浏览器驱动对象
        if cls._driver is None:
            cls._driver = webdriver.Chrome()
            cls._driver.maximize_window()
            cls._driver.implicitly_wait(10)
        return cls._driver

    # 问题 如何退出浏览器驱动对象呢?
    #     定义一个类属性,专门用来保存浏览器驱动对象
    #     如果类属性为空,则不做任何处理
    #     如果类属性非空,退出浏览器驱动对象,同时把类属性置空,不影响下次创建
    @classmethod
    def quit_driver(cls):
        if cls._driver is not None:
            time.sleep(2)
            cls._driver.quit()
            cls._driver = None


# 定义获取弹出框的提示消息工具方法
def get_tips_msg():
    time.sleep(2)
    return DriverUtil.get_driver().find_element_by_class_name('layui-layer-content').text
