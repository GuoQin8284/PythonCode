# 1.导包
import time
from selenium import webdriver
# 2.启动浏览器
web = webdriver.Chrome()
# 3.输入网址
web.get("http://192.168.13.195/")
# 4.等待3s
time.sleep(3)
# 5.关闭浏览器
web.quit()