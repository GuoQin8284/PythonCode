from tp_shop.unit_test import UnitDriver


class Base_page():

    def __init__(self):
        self.driver=UnitDriver.setup()

    def base_page(self,location):
        return self.driver.find_element(location[0],location[1])


class Base_handle():

    def base_handle(self,element,send):
        element.clear()
        element.send_keys(send)