from page.message_list import MessageList


class Page():
    def __init__(self,driver):
        self.driver=driver
    @property
    def message(self):
        return MessageList(self.driver)
