from urllib.request import *
from urllib.error import *
# username='username'
# password='password'
# # url='http://localhost:5000/'
#
# url1='http://www.baidu.com'
# p=HTTPPasswordMgrWithDefaultRealm()
# p.add_password(None,url1,username,password)
# auth_handler=HTTPBasicAuthHandler(p)
# opener=build_opener(auth_handler)
#
# result=opener.open(url1)
# html=result.read().decode('utf-8')
# print(html)


username='username'
password='password'
url='http://www.baidu.com'

p=HTTPPasswordMgrWithDefaultRealm()
p.add_password(None,url,username,password)
auth_handlers=HTTPBasicAuthHandler(p)
opener=build_opener(auth_handlers)

result=opener.open(url)
print(result.read().decode('utf-8'))
