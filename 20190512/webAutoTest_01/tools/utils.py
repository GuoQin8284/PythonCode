import time
from selenium import webdriver


class DriverUnit():
    _driver=None
    _quit_driver=True
    @classmethod
    def setup_driver(cls):
        if cls._driver is None:
            cls._driver=webdriver.Chrome()
            cls._driver.maximize_window()
            cls._driver.implicitly_wait(10)
        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver and cls._quit_driver:
            time.sleep(3)
            cls._driver.quit()

    @classmethod
    def set_quit_driver(cls,auto_quit):
        cls._quit_driver=auto_quit