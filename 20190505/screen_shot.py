import time

from selenium import webdriver

print(time.strftime("%Y%m%d-%H%M%S"))
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("file:///C:/Users/GQ/Desktop/page1/%E6%B3%A8%E5%86%8CA.html")
driver.find_element_by_id("userA").send_keys("admin")
time.sleep(0.3)
img_file="./img/IMG{}.png".format(time.strftime("%Y%m%d-%H%M%S%z"))
driver.get_screenshot_as_file(img_file)
driver.quit()