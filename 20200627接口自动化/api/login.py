import logging

import requests

import config


class Login:

    def __init__(self):
        self.login_url = config.host + r"/usercenter/v1.0/user/login"

    def login(self, res_data):
        self.request_data = res_data
        logging.info("请求的参数:{}".format(self.request_data))
        logging.info("请求的url:{}".format(self.login_url))
        return requests.post(url=self.login_url, json=self.request_data)