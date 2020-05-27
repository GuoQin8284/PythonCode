import time
from selenium import webdriver
from selenium.webdriver import ActionChains

dr= webdriver.Chrome()
dr.get("file:///C:/Users/GQ/Desktop/page1/%E6%B3%A8%E5%86%8CA.html")
action=ActionChains(dr)
# action.context_click(dr.find_element_by_css_selector("#userA")).perform()
action.move_to_element(dr.find_element_by_xpath("/html/body/div/fieldset/form/p[5]/button")).perform()
time.sleep(3)
dr.quit()