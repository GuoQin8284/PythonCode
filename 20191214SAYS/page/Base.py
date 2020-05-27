from driver.SaysDriver import UnitDriver


class Base_page():

    def __init__(self,url):
        self.driver=UnitDriver.SetupDriver(url)
    def find_element(self,element):
        return self.driver.find_element(element[0],element[1])

class Base_handle():


    def Input_text(self,element,text):
        element.clear()
        element.send_keys(text)

    def Click(self,element):
        element.click()