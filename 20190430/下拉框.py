import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

dr = webdriver.Chrome()
dr.get("file:///C:/Users/GQ/Desktop/page1/%E6%B3%A8%E5%86%8CA.html")
select = Select(dr.find_element_by_css_selector("#selectA"))
time.sleep(2)
select.select_by_index(1)
time.sleep(2)
select.select_by_value("sh")
time.sleep(2)
select.select_by_visible_text("A深圳")
time.sleep(2)
dr.quit()
