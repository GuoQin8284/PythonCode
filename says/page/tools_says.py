from selenium.webdriver.common.by import By

from driver.action import Action


class Says_page(Action):
    def __init__(self,driver):
        super().__init__(driver)
        self.says1=(By.XPATH,'//*[@id="Duoyue"]/div/div[1]/div/section/div[1]/div[1]/ul/li[2]')
        self.path='//*[@id="Duoyue"]/div/div[1]/div/section/div[1]/div[1]/'
        # 生产环境
        self.production_periodical = (By.XPATH, self.path+'section[1]/ul/li[2]')
        self.production_platform = (By.XPATH, self.path+'section[1]/ul/li[3]')
        self.production_author = (By.XPATH, self.path+'section[1]/ul/li[4]')
        self.production_says = (By.XPATH, self.path+'section[1]/ul/li[5]')
        # uat环境
        self.uat_periodical=(By.XPATH,self.path+'section[2]/ul/li[2]')
        self.uat_platform = (By.XPATH,self.path+'section[2]/ul/li[3]')
        self.uat_author = (By.XPATH,self.path+'section[2]/ul/li[4]')
        # 测试环境
        self.test_periodical=(By.XPATH,self.path+'section[3]/ul/li[2]')
        self.test_platform=(By.XPATH,self.path+'section[3]/ul/li[3]')
        self.test_anthor=(By.XPATH,self.path+'section[3]/ul/li[4]')
        self.test_says=(By.XPATH,self.path+'section[3]/ul/li[5]')
        # 元素列表
        self.ele_list=[self.production_periodical,self.production_platform,self.production_author,self.production_says,
                       self.uat_periodical,self.uat_platform,self.uat_author,
                       self.test_periodical,self.test_platform,self.test_anthor,self.test_says]

    # 测试环境元素返回
    def ele_says(self):
        return self.find_element(self.says1)

    def element(self,n):
        return self.find_element(self.ele_list[n])

class Says_handle(Says_page):
    def click_says(self):
        self.ele_says().click()
    def click_element(self,n):
        self.element(n).click()

class Says_proxy(Says_handle):
    def says(self):
        self.click_says()

    def click_says_element(self,n):
        self.click_element(n)
        print("n:",n)