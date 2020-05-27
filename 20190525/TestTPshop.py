import json
import unittest


import requests
from parameterized import parameterized

from base import BaseTPshop

def mydata():
    with open("./loginJson.json","r",encoding="utf-8") as f:
        data_list=[]
        data=json.load(f)
        # print(data)
        data1=data.get("user1")
        for a in data1:
            data_list.append((a.get("username"),
                             a.get("password"),
                             a.get("verify_code")))
        print(data_list)
        print(type(data_list))
    return data1

class TestTPshop(unittest.TestCase):

    def setUp(self):
        self.session=requests.Session()
        self.login=BaseTPshop()

    def tearDown(self):
        self.session.close()

    def test_1verify(self):
        respouse = self.login.get_verify(self.session)
        print(respouse.headers)

    @parameterized.expand(mydata())
    def test_2login(self,user,pwd,verify):
        data={"username":user,"password":pwd,"verify_code":verify}
        print("data",data)
        self.test_1verify()
        respouse = self.login.login1(self.session,data)
        print(respouse.status_code)


    def test_3order(self):
        self.test_2login()
        respouse = self.login.order(self.session)
        print(respouse.text)