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
driver.get("file:///C:/Users/iambtree/Desktop/page/%E6%B3%A8%E5%86%8CA.html")

# 3.业务操作
# 找到元素,操作元素
# 打开注册A页面 --用户名中输入 admin
driver.find_element_by_id("userA").send_keys("admin")
driver.find_element_by_id("passwordA").send_keys("123456")
# 截图保存


# pic_name = "./a.png"
# 图片名字不同  --  在文件名字中加入时间字符串  -- 年月日时分秒  "20190216154823"
# 何如把时间字符串放入文件命中 -- 字符串格式化   "a%s.png" %  "20190216154823"
# pic_name = "./a%s.png" % "20190216154823"
# 自动获取时间字符串的方法
# time.strftime("%Y%m%d%H%M%S")

# 动态图片文件名
# pic_name = "./a%s.png" % time.strftime("%Y%m%d%H%M%S")
# driver.get_screenshot_as_file(pic_name)

# 4.关闭浏览器
# 驱动对象调用quit()
time.sleep(2)
driver.quit()
