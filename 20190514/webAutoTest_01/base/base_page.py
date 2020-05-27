from units import DriverUnits


class BasePage():
    def __init__(self):
        self.driver=DriverUnits.driver_setup()
    def find_element(self,location):
        print("location[0]:{},location[1]:{}".format(location[0], location[1]))
        return self.driver.find_element(location[0],location[1])

class BaseHandle():
    def input_text(self,element,text):
        element.clear()
