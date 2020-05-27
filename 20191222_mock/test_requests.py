#登录接口https://adviser.osid.org.cn/usercenter/v1.0/user/login

# 获取信息https://adviser.osid.org.cn/usercenter/v1.0/user/getInfo

# 获取OSID列表https://adviser.osid.org.cn/channelcenter/v1.0/osid/osidList?numPerPage=10&currentPage=0
import json

import requests
session=requests.session()

respouse1 = session.post(url='https://adviser.osid.org.cn/usercenter/v1.0/user/login',json={"loginName":"15549080517","pwd":"e267cfcd18461ce938067eca67c59f41","isRemember":1,"systemCode":"adviser"})
print(respouse1.headers)
print(respouse1.status_code)
print(respouse1.text)
print(respouse1.json())
print(respouse1.content)
token=respouse1.json().get('data').get('token')
print(token)
print("*"*100)
param={"token":token}
print("param=",param)
respouse2=session.get(url='https://adviser.osid.org.cn/usercenter/v1.0/user/getInfo',headers=param)
# respouse2=session.get(url='https://adviser.osid.org.cn/usercenter/v1.0/user/getInfo')
print(respouse2.status_code)
print(respouse2.content)
print(respouse2.text)
print("*"*100)

param1={"numPerPage":10,"currentPage":0}
respouse3=session.get(url='https://adviser.osid.org.cn/channelcenter/v1.0/osid/osidList',params=param1,headers=param)
assert(100,respouse3.status_code)
print(respouse3.status_code)
print(respouse3.text)