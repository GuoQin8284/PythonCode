import http.cookiejar,urllib.request

cookie=http.cookiejar.CookieJar()
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
result=opener.open('http://www.baidu.com')
print(cookie)
for item in cookie:
    print(item)
    print(type(item))
    print(item.name+'='+item.value)