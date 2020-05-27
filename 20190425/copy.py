a = open("./readme","a+")
c = input("输入：")
while c != "exit":
    a.write(c.upper())
    c = input("输入：")
else:
    a.close()
b = open("./readme",'r')
print(b.read())