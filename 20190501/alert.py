import time
from selenium import webdriver

dr = webdriver.Chrome()
dr.get("file:///C:/Users/GQ/Desktop/page1/%E6%B3%A8%E5%86%8CA.html")
dr.find_element_by_id("alerta").click()
time.sleep(2)
alert = dr.switch_to.alert
time.sleep(2)
alert.accept()
dr.find_element_by_id("confirma").click()
time.sleep(2)
alert.dismiss()
time.sleep(2)
dr.find_element_by_id("prompta").click()
time.sleep(2)
print(alert.text)
alert.send_keys("admin")
time.sleep(2)
alert.accept()
time.sleep(2)
dr.quit()