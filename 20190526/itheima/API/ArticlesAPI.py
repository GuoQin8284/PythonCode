import requests


class Article():

    def __init__(self):
        self.url="http://ttapi.research.itcast.cn/app/v1_0/articles"

    def get_articles_id(self,id):
        my_param={"channel_id":id}
        respones=requests.get(self.url,params=my_param)
        return respones