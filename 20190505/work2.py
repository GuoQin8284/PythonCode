# 2. 对TPshop网站，使用cookie方式跳过验证码登录系统。[了解]
# 	关键cookie  "PHPSESSID"  "user_id"  "uname"


from selenium import webdriver

driver=webdriver.Chrome()
driver.get("http://localhost")
a = driver.get_cookies()
print(a)
# for cookies in a:
#     driver.add_cookie({"name":cookies.get("name"),"value":cookies.get("value"),"path":cookies.get("path")})
driver.add_cookie({"name":"PHPSESSID","value":"r8a90d8329do4grvu224kg9900","path":"/"})
driver.add_cookie({"name":"uname","value":"18012345678","path":"/"})
driver.add_cookie({"name":"user_id","value":"2601","path":"/"})
print(driver.get_cookies())
driver.refresh()
