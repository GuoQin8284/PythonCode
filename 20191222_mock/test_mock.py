import unittest
from unittest import mock


# def login(a, b):
#     return False

class Unit(unittest.TestCase):

    def test01(self):
        login1=mock.Mock(return_value=True)

        abc=login1('110','444')
        print("he=",abc)
        print(type(abc))
        print(login1.called)
        print(login1.call_count)

#
# from unittest import mock
#
# from pip._vendor import requests
#
#
# def request_baidu():
#     resp = requests.get('http://www.baidu.com')
#     return resp.status_code
#
# # 模拟调用request_baidu，且返回值是500
# request_baidu1 = mock.Mock(return_value=500)
# print(request_baidu())
# print(request_baidu1.called)#打印是否被调用
# print(request_baidu1.call_count)#打印调用次数
