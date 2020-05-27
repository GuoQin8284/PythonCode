import json
import unittest

from parameterized.parameterized import parameterized

from itheima.API.loginAPI import Login
from itheima.app import TOKEN


def data_list():
    data=[]
    with open("../data/login_case.json","r",encoding="utf-8") as f:
        vs = json.load(f)
        print("vs",vs)
        for v in vs.values():
            data.append((v.get("mobile"),
            v.get("code"),
            v.get("status_code"),
            v.get("message"))
            )

    return data


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.login=Login()
    def test_get_verify_code(self):
        self.login.get_verify_code("15549080517")

    @parameterized.expand(data_list())
    def test_login(self,mobile,code,status_code,message):
        print(mobile)
        print(code)
        print(status_code)
        print(message)

        respouse=self.login.login(mobile,code)

        self.assertEqual(respouse.status_code,status_code)
        print("json:",respouse.json())
        result=respouse.json().get("message")
        self.assertIn(message,result.get("mobile"))

    def test_login_suceess(self):
        # a = input("输入验证码：")
        respouse=self.login.login("15549080517","350609")
        try:
            token= respouse.json().get("data").get("token")
            TOKEN = token
        except Exception as e:
            print("登录失败没有返回token")
            raise e

        self.assertEqual("201",respouse.status_code)
        self.assertEqual("OK",respouse.text)