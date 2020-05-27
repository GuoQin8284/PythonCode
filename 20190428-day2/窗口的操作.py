import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("file:///C:/Users/GQ/Desktop/page1/%E6%B3%A8%E5%86%8CA.html")
driver.maximize_window()
time.sleep(2)
driver.set_window_size(500,700)
time.sleep(2)
driver.set_window_position(300,300)
time.sleep(2)
driver.quit()
