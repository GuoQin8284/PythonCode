import requests

from itheima.app import BASE_URl


class Login():

    def __init__(self):
        self.get_verify_code_url=BASE_URl+"app/v1_0/sms/codes/"
        self.login_url = BASE_URl + "app/v1_0/authorizations"
        self.channels_url="http://ttapi.research.itcast.cn/app/v1_0/user/channels"
    #
    def get_verify_code(self,mobile):
        respouse=requests.get(self.get_verify_code_url+mobile)
        return respouse

    def login(self,mobile,code):
        myjson={}
        if mobile:
            myjson["mobile"]=mobile

        if code:
            myjson["code"]=code

        respouse=requests.post(self.login_url,myjson)
        return respouse

