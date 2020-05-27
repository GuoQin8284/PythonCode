import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

dr = webdriver.Chrome()
dr.get("file:///C:/Users/GQ/Desktop/page1/%E6%B3%A8%E5%86%8CA.html")

time.sleep(2)
ActionChains(dr).move_to_element(dr.find_element_by_xpath("/html/body/div/fieldset/form/p[5]/button"))
dr.find_element_by_id("alerta").click()
time.sleep(2)
alert = dr.switch_to.alert
alert.accept()
a = dr.find_element_by_id("userA")
a.send_keys("admin")
time.sleep(2)
a.send_keys(Keys.CONTROL,"a")
a.send_keys(Keys.CONTROL,"c")
time.sleep(2)
dr.find_element_by_id("passwordA").send_keys(Keys.CONTROL,"v")
time.sleep(1)
dr.execute_script("window.scrollTo(0,100000)")
time.sleep(1)
select=Select(dr.find_element_by_id("selectA"))
select.select_by_index(3)
time.sleep(1)
select.select_by_value("gz")
time.sleep(1)
select.select_by_visible_text("A上海")
time.sleep(1)
print(dr.find_element_by_id("userA").is_displayed())


time.sleep(2)
dr.quit()
