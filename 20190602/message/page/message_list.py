from selenium.webdriver.common.by import By

from base.action import BaseAction


class MessageList(BaseAction):


    NewMessage_btn=By.XPATH,"//*[@content-desc='新信息']"

    ReceiveNum_btn=By.XPATH,"//*[@text='接收者']"

    Content_ele=By.XPATH,"//*[@text='键入信息']"

    Send_btn=By.XPATH,"//*[@content-desc='发送']"

    def click_NewMessage(self):
        self.click(self.NewMessage_btn)

    def input_ReceiveNum_btn(self,Phone_num):
        self.input(self.ReceiveNum_btn,Phone_num)

    def input_content(self,content):
        self.input(self.Content_ele,content)

    def send_message(self):
        self.click(self.Send_btn)