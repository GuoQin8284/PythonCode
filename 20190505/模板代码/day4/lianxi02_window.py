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
# 打开‘注册实例.html’页面，完成以下操作

# 1).注册实例-- 点击‘注册A页面’链接， 注册A网页  click
driver.find_element_by_link_text("注册A页面").click()
time.sleep(2)

# 切换窗口

# a.所有窗口


# b.目标窗口
# 没有切换  --  知道当前的句柄是什么  ---  不是当前的---就是目标


# c.切换窗口


# d.当前窗口



# 2). 注册A网页---在打开的页面，填写A页面注册信息；    userA   admin
driver.find_element_by_id("userA").send_keys("admin")



# 4.关闭浏览器
# 驱动对象调用quit()
time.sleep(2)
driver.quit()
