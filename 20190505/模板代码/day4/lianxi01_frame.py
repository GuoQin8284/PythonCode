# selenium webdriver
import time

# 0.导入自动化测试工具
from selenium import webdriver

# 1.打开浏览器
# 实例化浏览器驱动对象
# obj = 类名()
driver = webdriver.Chrome()

# 2.输入网址
# 驱动对象调用get("协议://URL")
driver.get("file:///C:/Users/iambtree/Desktop/page/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html")

# 3.业务操作
# 找到元素,操作元素
# frame切换
# 案例：打开‘注册实例.html’页面，完成以下操作
# 用户名  admin
# 1. 填写主页面的注册信息
driver.find_element_by_id("user").send_keys("admin")
time.sleep(2)


# A子页 --  A子页iframe 标签的信息
# a.主页--子页 --iframe -- id


# b.子页操作    A子页 --- 输入操作
# 2. 填写注册页面A中的注册信息



# c.子页--主页



# B子页 中输入内容
# a.主页--子页 --iframe -- name


# b.子页操作   B子页中的业务操作
# # 3. 填写注册页面B中的注册信息



# c.子页--主页




# 4.关闭浏览器
# 驱动对象调用quit()
time.sleep(2)
driver.quit()
