import time
from selenium import webdriver


class DriverUnit():
    _driver=None
    @classmethod
    def setup(self):
        if self._driver is None:
            self._driver = webdriver.Chrome()
            self._driver.maximize_window()
            self._driver.implicitly_wait(10)
            self._driver.get("http://172.16.64.1/WebAuth_auth.asp?ip=192.168.13.85&9313c")
            self._driver.find_element_by_css_selector("#userName").send_keys("ruanjianceshi01")
            self._driver.find_element_by_css_selector("#userPasswd").send_keys("19879164")
            self._driver.find_element_by_css_selector("input[name='configSubmit']").click()
            self._driver.get("http://cal.apple886.com/")
        return self._driver

    @classmethod
    def quit(self):
        time.sleep(3)
        self._driver.quit()
