import unittest

import time
from selenium import webdriver


class DriverUnit(unittest.TestCase):
    _driver=None
    @classmethod
    def unit_setup(cls):
        if cls._driver is None:
            cls._driver=webdriver.Chrome()
            cls._driver.maximize_window()
            cls._driver.implicitly_wait(10)
        return cls._driver
    @classmethod
    def unit_quit(cls):
        time.sleep(2)
        cls._driver.quit()
