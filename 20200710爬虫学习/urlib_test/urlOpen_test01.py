from urllib import request

url="https://www.python.org"
response = request.urlopen(url=url)

print(type(response))
print(response.status)
print(response.getheaders())
print(response.read().decode("utf- 8"))