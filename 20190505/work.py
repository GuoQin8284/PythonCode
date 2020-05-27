# 1. 打开TPshop网站首页，完成以下操作：
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
print(time.strftime("%Y%m%d%H%M%S"))
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(8)
driver.get("http://localhost")
#     1. 点击‘登录’跳转到登录页面
driver.find_element_by_link_text("登录").click()
#     2. 输入用户名、密码和万能验证码，点击登录按钮进入后台管理页面
driver.find_element_by_id("username").send_keys("18012345678")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("verify_code").send_keys("8888")
driver.find_element_by_link_text("登    录").click()
#     3. 选择‘账户设置’下的‘收货地址’选项
ActionChains(driver).move_to_element(driver.find_element_by_xpath("//div[@class='u-dt']/span")).perform()
driver.find_element_by_link_text("收货地址").click()
#     4. 点击地址管理下的‘增加新地址’按钮
driver.find_element_by_xpath("//span[@class='co_blue' and text()='增加新地址']").click()
#     5. 输入地址信息，收货地址选择‘上海市-市辖区-浦东新区-三林镇’，其他选项任意输入
driver.switch_to.frame("layui-layer-iframe100001")
driver.find_element_by_css_selector("input[class='wi80-BFB'").send_keys("铁蛋儿")
Select(driver.find_element_by_id("province")).select_by_visible_text("上海市")
Select(driver.find_element_by_id("city")).select_by_visible_text("市辖区")
Select(driver.find_element_by_id("district")).select_by_visible_text("浦东新区")
Select(driver.find_element_by_id("twon")).select_by_visible_text("三林镇")
driver.find_element_by_id("address").send_keys("黄浦江中心")
driver.find_element_by_xpath("//input[@class='wi40-BFB' and @name='mobile']").send_keys("18012345678")
#     6. 点击‘保存收货地址’按钮
driver.find_element_by_xpath("//span[text()='保存收货地址']").click()
#     7. 关闭当前窗口
driver.quit()
print(time.strftime("%Y%m%d%H%M%S"))
#     要求：
#         1. 每执行一个操作暂停2秒，方便观看效果
#         2. 在浏览器窗口最大化的状态下操作，设置隐式等待为30秒