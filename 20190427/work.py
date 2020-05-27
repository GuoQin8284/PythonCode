"""
2. 自己动手编写脚本，实现以下功能：
    1. 启动火狐浏览器
    2. 打开百度网站：http://www.baidu.com
    3. 暂停3秒
    4. 打开淘宝网站：http://www.taobao.com
    5. 暂停3秒
    6. 关闭浏览器
    要求：代码干净整洁、有注释
"""
# # 导入模块
# import time
# from selenium import webdriver
# # 打开浏览器（创建浏览器对象）
# driver = webdriver.Chrome()
# # 业务操作（打开网址）
# driver.get("http://www.baidu.com")
# # 等待
# time.sleep(3)
# # 业务操作（打开网址）
# driver.get("http://www.taobao.com")
# # 等待
# time.sleep(3)
# # 结束，关闭浏览器
# driver.quit()

"""
3. 打开TPshop网站首页，完成登录操作，具体步骤如下：
    1. 点击页面顶部的‘登录’链接，进入登录页面
    2. 输入用户名：13012345678
    3. 输入密码：123456
    4. 输入验证码：8888
    5. 点击登录按钮
    6. 暂停10秒
    要求：元素定位方式不做限制
"""
# import time
# from selenium import webdriver
# tdriver = webdriver.Chrome()
# tdriver.get("http://localhost")
# tdriver.find_element_by_class_name("red").click()
# time.sleep(5)
# tdriver.find_element_by_id("username").send_keys("13012345678")
# tdriver.find_element_by_id("password").send_keys("123456")
# tdriver.find_element_by_id("verify_code").send_keys("8888")
# tdriver.find_element_by_name("sbtbutton").click()
# time.sleep(10)
# tdriver.quit()