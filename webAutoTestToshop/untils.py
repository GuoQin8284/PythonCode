from selenium import webdriver


class DeiverUnilt():
    _driver=None
    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            cls._driver=webdriver.Chrome()
            cls._driver.maximize_window()
            cls._driver.implicitly_wait(10)
            cls._driver.get("http://localhost")
        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver:
            cls._driver.quit()
            cls._driver=None