import urllib.request
import urllib.parse
data=bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf-8')

respouse=urllib.request.urlopen('http://httpbin.org/post',data=data,timeout=0.1)


print(respouse.read().decode('utf-8'))
print(respouse.getheaders())
print(respouse.getheader('server'))
print(type(respouse))