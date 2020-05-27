from selenium import webdriver


# 创建驱动类
class Driver():
    @classmethod
    def driver(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        return self.driver