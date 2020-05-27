
# 1、打开TPshop网站首页，完成以下操作：
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://localhost")
    # 1.使用id定位方式定位到搜索框，并输入内容‘1’
driver.find_element_by_id("q").send_keys("1")

    # 2.使用name定位方式定位到搜索框，并输入内容‘2’
driver.find_element_by_name("q").send_keys("2")
    # 3.使用class_name定位方式定位到搜索框，并输入内容‘3’
driver.find_element_by_class_name("ecsc-search-input").send_keys("3")
    # 4.使用tag_name定位方式定位到搜索框，并输入内容‘4’
driver.find_element_by_tag_name("input").send_keys("4")
    # 5.使用xpath定位方式定位到搜索框，并输入内容‘5’
driver.find_element_by_xpath("//*[@id='q']").send_keys("5")
    # 6.使用css定位方式定位到搜索框，并输入内容‘6’
driver.find_element_by_css_selector("input#q").send_keys('6')
    # 7.暂停3秒
time.sleep(3)
driver.quit()

