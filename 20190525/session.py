# 需求：使用requests库调用TPshop登录功能的相关接口，完成登录操作，登录成功后获取'我的订单'页面
#相关接口：
#     获取验证码：http://localhost/index.php?m=Home&c=User&a=verify
#     登录：http://localhost/index.php?m=Home&c=User&a=do_login
#     登录提交数据{"username":"13800001111", "password":"123456", "verify_code": 8888}
#     我的订单：http://localhost/Home/Order/order_list.html
#

import requests

session=requests.Session()

respous=session.get("http://localhost/index.php?m=Home&c=User&a=verify")

mydata={"username":"18012345678", "password":"123456", "verify_code": 8888}

respous1=session.post("http://localhost/index.php?m=Home&c=User&a=do_login",data=mydata)

respous2=session.get("http://localhost/Home/Order/order_list.html")

print(respous2.text)

