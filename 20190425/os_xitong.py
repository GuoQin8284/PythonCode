# 1.	创建一个目录newdir并切换到该目录下，切换完成后调用getcwd()显示以下工作目录的信息。
import os
a = os.listdir()
print(a)
# os.mkdir("newdir")
# a = os.getcwd()
# print(a)
c = os.chdir("newdir")
print(c)
a = os.getcwd()
print(a)
c=os.chdir(".")
print(c)
# # 2.	手动在newdir目录下创建3个文件test_1.txt、test_2.txt、test_3.txt，修改文件名称，在三个文件名前均添加“bkup_”信息。
# # a = open("test_1.txt","w")
# # a.close()
# # b = open("test_2.txt","w")
# # b.close()
# # c = open("test_3.txt","w")
# # c.close()
# # os.remove("./test_1.txttest_1.txttest_1.txt")
#
d = os.listdir("./")
print(d)
# for name in d:
#     print(name)
#     # if name==".idea":
#     #     continue
#     # new_name=name[5:]
#     os.rename(name,"bkup_"+name)