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
driver.get("https://www.baidu.com")

# 3.业务操作
# 找到元素,操作元素


# 获取所有cookie


# 获取单个cookie


# 添加cookie

# 添加后查看对应cookie信息




# 4.关闭浏览器
# 驱动对象调用quit()
time.sleep(2)
driver.quit()
