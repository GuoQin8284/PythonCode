import json
import time
from selenium import webdriver

from config import json_file


def test_case_json():
    with open(json_file + "/test_json/login_case.json", "r", encoding="UTF-8") as f:
        json_data = json.load(f)
        return json_data


class DriverUnits():
    _driver=None
    _auto_quit=True
    @classmethod
    def driver_setup(self):
        if self._driver is None:
            self._driver=webdriver.Chrome()
            self._driver.maximize_window()
            self._driver.implicitly_wait(10)
        return self._driver
    @classmethod
    def driver_quit(cls):
        if cls._driver is not None and cls._auto_quit:
            time.sleep(3)
            cls._driver.quit()

    @classmethod
    def set_auto_quit(cls,auto):
        cls._auto_quit=auto
