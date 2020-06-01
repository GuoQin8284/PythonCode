from selenium.webdriver.common.by import By

from base.base_action import Action


class SaveContact(Action):
    contact_tittl = By.ID, "com.android.contacts:id/large_title"
    contact_phone = By.ID, "com.android.contacts:id/header"

    def get_contact_tittl(self):
        contact_text = self.find_element(self.contact_tittl).text
        return contact_text

    def get_contact_phone(self):
        contact_phone = self.find_element(self.contact_phone).text.replace(" ","").replace("-","")
        return int(contact_phone)