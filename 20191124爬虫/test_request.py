import urllib.request
import urllib.parse

# request=urllib.request.Request('http://httpbin.org')
# respouse=urllib.request.urlopen(request)
# print(respouse.read().decode('utf-8'))

url='http://httpbin.org/post'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'host':'httpbin.org'
}
dict={
    'name':'hhaha'
}
data=bytes(urllib.parse.urlencode(dict),encoding='utf-8')
# requset=urllib.request.Request(url=url,data=data,headers=headers,method='POST')
requset=urllib.request.Request(url=url,data=data,method='post')
requset.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36)')
response=urllib.request.urlopen(requset,timeout=2)
print(response.read().decode('utf-8'))