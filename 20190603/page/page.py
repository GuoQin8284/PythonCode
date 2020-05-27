from page.contact import Contact


class Page():

    def __init__(self,driver):
        self.driver=driver

    @property
    def contact(self):
        return Contact(self.driver)