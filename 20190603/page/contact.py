from selenium.webdriver.common.by import By

from base.base_action import Action


class Contact(Action):

    add_contact=By.XPATH,"//*[@content-desc='添加新联系人']"

    contact_name=By.XPATH,"//*[@text='姓名']"

    contact_num=By.XPATH,"//*[@text='电话']"

    local_save=By.XPATH,"//*[@text='本地保存']"

    def click_contact(self):
        self.click(self.add_contact)

    def input_name(self,name):
        self.input(self.contact_name,name)

    def input_num(self,num):
        self.input(self.contact_num,num)

    def click_local_save(self):
        try:
            if self.find_element(self.local_save).text:
                self.click(self.local_save)

        except Exception as f:
            pass
