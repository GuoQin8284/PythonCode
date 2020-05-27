from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class PageAddPhoneNum(BaseAction):

    AddContact=By.XPATH,"//*[@content-desc='添加新联系人']"

    LocalSave=By.XPATH,"//*[@text='本地保存']"

    PhoneName=By.XPATH,"//*[@text='姓名']"

    PhoneNum = By.XPATH, "//*[@text='电话']"

    def injoin_contact(self):
        self.click(self.AddContact)

    def send_PhoneName(self,content):
        try:
            if self.find_element(self.LocalSave).text=="本地保存":
                self.click(self.LocalSave)

        # except Exception as e:
        #     print(e)

        finally:
            self.input(self.PhoneName,content)

    def send_PhoneNum(self,content):
        self.input(self.PhoneNum,content)


