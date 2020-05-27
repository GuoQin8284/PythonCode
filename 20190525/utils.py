# 需求：使用requests库调用TPshop登录功能的相关接口，完成登录操作，登录成功后获取'我的订单'页面
#相关接口：
#     获取验证码：http://localhost/index.php?m=Home&c=User&a=verify
#     登录：http://localhost/index.php?m=Home&c=User&a=do_login
#     登录提交数据{"username":"13800001111", "password":"123456", "verify_code": 8888}
#     我的订单：http://localhost/Home/Order/order_list.html
#

import unittest

import requests


class TestTPshop(unittest.TestCase):

    def setUp(self):
        self.session=requests.Session()

    def tearDown(self):
        self.session.close()

    def test_verify(self):
        verify=self.session.get("http://localhost/index.php?m=Home&c=User&a=verify")
        print(verify.status_code)

    def test_login(self):
        self.test_verify()
        mydata={"username":"18012345678", "password":"123456", "verify_code": 8888}
        login=self.session.post("http://localhost/index.php?m=Home&c=User&a=do_login",mydata)
        print(login.status_code)
        print(login.headers)

    def test_order(self):
        self.test_login()
        order=self.session.get("http://localhost/Home/Order/order_list.html")
        print(order.status_code)
        print(order.text)
