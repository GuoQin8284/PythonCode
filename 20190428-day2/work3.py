# . 打开TPshop网站首页，完成登录操作，具体步骤如下：
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://localhost")
#     1. 点击页面顶部的‘登录’链接，进入登录页面
driver.maximize_window()
driver.find_element_by_link_text("登录").click()
#     2. 输入用户名：13012345678
driver.find_element_by_id("username").send_keys("13012345678")
#     3. 输入密码：123456
driver.find_element_by_css_selector("#password").send_keys("123456")
#     4. 输入错误的验证码：0000
driver.find_element_by_xpath("//*[@placeholder='验证码']").send_keys("0000")
#     5. 点击登录按钮
driver.find_element_by_xpath("//*[@onclick='checkSubmit();']").click()
#     6. 获取提示框中的消息内容
time.sleep(2)
# a=driver.find_element_by_class_name('layui-layer-content')
a=driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[2]')
print(a.text)
#     7. 点击提示框的确定按钮
driver.find_element_by_xpath('//a[@class="layui-layer-btn0"]').click()
#     8. 重新输入正确的验证码：8888
driver.find_element_by_xpath("//*[@placeholder='验证码']").clear()
driver.find_element_by_xpath("//*[@placeholder='验证码']").send_keys("8888")
#     9. 点击登录按钮
time.sleep(2)
driver.find_element_by_xpath("//*[@onclick='checkSubmit();']").click()
#     10. 暂停5秒
time.sleep(5)
#     11. 打印当前页面的标题
print(driver.title)
#     要求：只能使用Xpath和CSS定位方式，在浏览器窗口最大化的状态下操作
time.sleep(3)
driver.quit()