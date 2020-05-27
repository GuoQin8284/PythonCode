import os


# a=os.getcwd()
# print(a)
# b=os.listdir('../copyfile')
# for i in b:
#     print(i)
#     if i=='__init__.py':
#         os.remove(i)
#         print(os.listdir('../copyfile'))


# try:
#     isExists=os.path.exists('../data')
#     print("is:",isExists)
#     if isExists:
#         print("文件夹已存在")
#         # os.makedirs(r"../data/a/b")
#         if os.path.exists('../data/a/b'):
#             os.rmdir('../data/a/b')
#     else:
#         os.mkdir('../data')
#         print("文件夹已创建")
# except Exception as e:
#     print(e)

a = os.path.isfile('../copyfile/data.wmv')
b = os.path.isdir('../copyfile/data.wmv')
print(a)
print(b)