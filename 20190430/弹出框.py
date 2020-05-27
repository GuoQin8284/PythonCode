import time
from selenium import webdriver

dr = webdriver.Chrome()
dr.get("file:///C:/Users/GQ/Desktop/page1/%E6%B3%A8%E5%86%8CA.html")
# 确认

# dr.find_element_by_css_selector("#alerta").click()
#
# time.sleep(2)
# a = dr.switch_to.alert
# print("alert:",a.text)
#
# a.dismiss()
# # a.accept()
# dr.quit()

# 取消
time.sleep(3)
dr.find_element_by_css_selector("#confirma").click()
a = dr.switch_to.alert
print("text：",a.text)
time.sleep(3)
a.dismiss()
time.sleep(3)
dr.quit()