from selenium.webdriver.common.by import By

from base.action_base import ActionBase


class Me(ActionBase):

    # "我"的特征
    me_button = By.ID, "com.yunmall.lc:id/tab_me"

    def click_me_button(self):
        pass
