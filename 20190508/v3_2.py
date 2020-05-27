import time
from selenium import webdriver

class Driver(object):
    _driver=None
    @classmethod
    def driver_setup(self):
        if Driver._driver is None:
            self._driver = webdriver.Chrome()
            self._driver.maximize_window()
            self._driver.implicitly_wait(15)
            self._driver.get("http://localhost")
        return self._driver
    @classmethod
    def driver_quit(self):
        time.sleep(3)
        if self._driver is not None:
            self._driver.quit()
            self.driver=None

    def driver_text(self):
        text=self._driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[2]').text
        return text