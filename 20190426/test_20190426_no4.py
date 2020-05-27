# 通过循环创建十个文件，命名为1.txt，2.txt，3.txt....
# 然后将文件名修改为：副本1.txt，副本2.txt，副本3.txt...
import os
os.mkdir("new")
os.chdir("new")
print(os.getcwd())
for a in range(1,11):
    name = open(str(a)+".txt","w")
    name.close()

b = os.listdir()
for name in b:
    os.rename(name,"副本"+name)
b = os.listdir()
print(b)


