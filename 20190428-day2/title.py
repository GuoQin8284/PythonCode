import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://localhost")
time.sleep(1)
print("title:",driver.title)
print("url",driver.current_url)
driver.quit()
