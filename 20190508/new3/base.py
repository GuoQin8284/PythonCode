from new3.unit_test import DriverUnit


class Base_page():
    def __init__(self):
        self.driver = DriverUnit().unit_setup()
    def find_element(self,location):
        return self.driver.find_element(location[0],location[1])

class Base_handle():
    def input_text(self,element,text):
        element.clear()
        element.send_keys(text)