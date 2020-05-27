from selenium.webdriver.support.wait import WebDriverWait


class ActionBase():

    def __init__(self,driver):
        self.driver=driver

    def find_element(self,feature,timeout=5,intver=0.5):
        return WebDriverWait(self.driver,timeout,intver).until(lambda x:x.find_element(feature[0],feature[1]))

    def click(self,feature):
        self.find_element(feature).click()

    def input(self,feature,content):
        self.find_element(feature).send_keys(content)

    def scroll_screen(self,direction="up"):
        width=self.driver.get_window_size()["width"]
        height = self.driver.get_window_size()["height"]
        center_x=width / 2
        center_y=height / 2

        left_x=width / 4
        left_y=center_y
        right_x=width / 4 * 3
        right_y=center_y

        up_x=center_x
        up_y=height / 4
        down_x=center_x
        down_y=height / 4 * 3

        if direction=="up":
            self.driver.swipe(down_x,down_y,up_x,up_y,2000)
        elif direction=="down":
            self.driver.swipe(up_x, up_y, down_x, down_y, 2000)
        elif direction == "left":
            self.driver.swipe(right_x, right_y, left_x, left_y, 2000)
        elif direction == "right":
            self.driver.swipe(left_x, left_y, right_x, right_y, 2000)
        else:
            print("输入错误：up/down/left/right")


    def scoll_find(self,feature):
        page_source=""
        while True:
            try:
                return self.find_element(feature)

            except:
                if self.driver.page_source==page_source:
                    print("到底了")
                    break
                else:
                    self.scroll_screen()
                    page_source
