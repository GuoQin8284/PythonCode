from selenium import webdriver
driver=webdriver.Chrome()
driver.get("file:///C:/Users/GQ/Desktop/page1/%E6%B3%A8%E5%86%8CA.html")
size=driver.find_element_by_css_selector('[name="userA"]').size
a=driver.find_element_by_css_selector("#fw")
text=a.text
url=a.get_attribute("href")
span=driver.find_element_by_css_selector("span").is_displayed()
cancel=driver.find_element_by_css_selector("#cancelA").is_enabled()
check=driver.find_element_by_css_selector("#lyA").is_selected()
print(size)
print(text)
print(url)
print(span)
print(cancel)
print(check)
driver.quit()