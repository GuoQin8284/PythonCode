# data=open("../data.txt",'rb')
#
# a=data.readline()
#
# print(a)
#
# data_write=open("../dataWrite.txt","wb+")
#
# data_write.write(a)
#
# data_write.seek(0)
# print("{}".format(data_write.read()))

a = open(r'D:\PythonCode\fileRead\SAYS产品7月第3周学习报告_郭钦_20190721.doc','rb')

print("%b",a.read())
a.seek(0)
b = open('./a.doc','wb+')
b.write(a.read())
b.seek(0)
print(b.read(10))

a.close()
b.close()