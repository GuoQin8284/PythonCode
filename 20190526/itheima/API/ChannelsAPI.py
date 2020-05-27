import requests


class Channels():

    def __init__(self):
        self.channels_url="http://ttapi.research.itcast.cn/app/v1_0/user/channels"

    def get_channels(self):
        respouse = requests.get(self.channels_url)
        return respouse