from selenium.webdriver.common.by import By

from base.action import Action


class DisplayPage(Action):

    search = By.ID, "com.android.settings:id/search"
    back = By.CLASS_NAME, "android.widget.ImageButton"
    input_edit_text = By.ID, "android:id/search_src_text"

    def click_search(self):
        self.click(self.search)

    def click_back(self):
        self.click(self.back)

    def input_text(self, text):
        self.input(self.input_edit_text,text)
