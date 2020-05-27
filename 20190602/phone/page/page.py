from page.page_add_phoneNum import PageAddPhoneNum


class Page():

    def __init__(self,driver):
        self.driver=driver
    @property
    def page_add_contact(self):
        return PageAddPhoneNum(self.driver)