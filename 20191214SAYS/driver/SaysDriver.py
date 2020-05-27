from selenium import webdriver



"""
says期刊PC端：https://adviser.osid.org.cn/
says作者PC端：https://author.osid.org.cn/
says平台端：https://platform.osid.org.cn/
"""
class UnitDriver():

    driver = None

    @classmethod
    def SetupDriver(cls,url):
        if cls.driver is None:
            cls.driver= webdriver.Chrome()
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(10)
            cls.driver.get(url)
        return cls.driver

    @classmethod
    def QuitDeiver(cls):
        if cls.driver is not None:
            cls.driver.quit()