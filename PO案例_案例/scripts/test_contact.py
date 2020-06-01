import pytest

from base.base_driver import baseDriver
from page.page_add_contact import AddContact
from page.page_contact import ContactList


class TestContact():

    def setup(self):
        self.driver = baseDriver(appPackage="com.android.contacts", appActivity="com.android.contacts.activities.PeopleActivity")
        self.pageContact = ContactList(self.driver)
        self.page_add_contact = AddContact(self.driver)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize(("contact_text", "phone"), [("德玛西亚", 15549080517),("peiqi", 18071102549)])
    def test_add_contact(self, contact_text, phone):
        self.pageContact.click_new_contact()
        # 判断当前是否出现保存提示
        if self.page_add_contact.is_toast():
            self.page_add_contact.click_local_save()
        self.page_add_contact.input_contact(contact_text)
        self.page_add_contact.input_phone(phone)
        # 返回保存
        self.page_add_contact.press_keyCode(4)