from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from base.base_action import Action


class AddContact(Action):
    get_toast = By.ID, "com.android.contacts:id/text"
    local_save = By.XPATH, "//*[@text='本地保存']"
    contact_edit_text = By.XPATH, "//*[@text='姓名']"
    phone_edit_text = By.XPATH, "//*[@text='电话']"

    def is_toast(self):
        try:
            toast = self.find_element(feature=self.get_toast, timeout=2).text
            if toast:
                return True
        except TimeoutException:
            return False

    def click_local_save(self):
        self.click(self.local_save)

    def input_contact(self, contact_text):
        self.input_text(self.contact_edit_text, contact_text)

    def input_phone(self, contact_phone):
        self.input_text(self.phone_edit_text, contact_phone)