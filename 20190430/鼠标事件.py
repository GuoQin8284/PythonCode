from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("http://localhost")
# a = driver.find_element_by_link_text("登录")
# action = ActionChains(driver)
# action.context_click(a).perform()
ActionChains(driver).context_click(driver.find_element_by_link_text("登录")).perform()

