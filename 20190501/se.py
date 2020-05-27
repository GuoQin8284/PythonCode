import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
dr=webdriver.Chrome()
# dr.get("file:///C:/Users/GQ/Desktop/page1/%E6%B3%A8%E5%86%8CA.html")
dr.get("file:///C:/Users/GQ/Desktop/page1/%E6%B3%A8%E5%86%8CA.html")
select = Select(dr.find_element_by_id("selectA"))
time.sleep(3)
select.select_by_index("0")
time.sleep(3)
select.select_by_value("sh")
time.sleep(3)
select.select_by_visible_text("A上海")
time.sleep(3)
dr.quit()