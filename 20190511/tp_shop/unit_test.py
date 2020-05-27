import time
from selenium import webdriver


class UnitDriver():
    _driver=None

    @classmethod
    def setup(self):
        if self._driver is None:
            self._driver=webdriver.Chrome()
            self._driver.maximize_window()
            self._driver.implicitly_wait(10)
            self._driver.get("http://localhost")
        return self._driver

    @classmethod
    def quit(self):
        time.sleep(2)
        self._driver.quit()
        self._driver=None