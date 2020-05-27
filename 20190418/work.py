"""
1.	定义字典元素的列表：stds_list = [
{"id": 1, "name": "小明", "c_s": 85, "python_s": 78},
{"id": 2, "name": "小花", "c_s": 69, "python_s": 88},
{"id": 3, "name": "小东", "c_s": 79, "python_s": 83},
]
1)	显示学生信息：“学生id：学生姓名：小明，C语言成绩：85, Python成绩：78”。
2)	修改“小明”的Python成绩为90
3)	删除“小东”的信息
"""
# stds_list = [
# {"id": 1, "name": "小明", "c_s": 85, "python_s": 78},
# {"id": 2, "name": "小花", "c_s": 69, "python_s": 88},
# {"id": 3, "name": "小东", "c_s": 79, "python_s": 83},
# ]
# for std in stds_list:
#     if std["name"]=="小明":
#         print("学生id：%s\n学生姓名：%s\nc语言成绩：%s\npython成绩：%s"%(std["id"],std["name"],std["c_s"],std["python_s"]))
#         std["python_s"]="90"
#         print(stds_list)
#     if std["name"]=="小东":
#         stds_list.remove(std)
#         print(stds_list)

#  2.	定义一个空列表，用于保存5个学生信息，一个学生信息包括三个属性：id、姓名、年龄
# name = input('姓名:')
# id = input('id:')
# age = input('年龄:')
#
# stu_list1 = []
# i = 1
# while i<=5:
#     name = input('姓名:')
#     id = input('id:')
#     age = input('年龄:')
#     stu_dict = {'name': name, 'id': id, 'age': age}
#     stu_list1.append(stu_dict)
#     i += 1
# print(stu_list1)

#  1.	从键盘上获取信息，判断是否可转换为数字，如果是，转换为整数。
# a = input('输入值：')
# if a.isdecimal():
#     print("可以转换为数字,转换后的数字为：%d" % int(a))

#  2.	输入一行字符,统计其中有多少个单词，每两个单词之间以空格隔开。如输入: This is a Python program.
#       输出：There are 5 words in the line
#  3.	计算字符串最后一个单词的长度，单词以空格隔开。（使用input()输入一个句子）
# a = input('输入值：')
# b = a.split( )
# print('There are',len(b),'words in the line')
# c=b[-1:-2:-1]
# print('最后一个单词长度为：',len(c[0]))

#  4.	从键盘输入一句话，输入的信息两端有空白字符。"  Life is short, you need python!   "
#       除去两端的空白字符，查找其中的python，将其替换为python3。

# a = input("输入：")
# b = a.strip()
# print('%s'% b.replace("python","python3"))


#  5.	完成字符串的逆序以及统计：
# 现有字符串： str1 = '1234567890'，根据题目要求，将截取后的新字符串赋值给str2




# # 截取字符串的第一位到第三位的字符
# str1 = '1234567890'
# str2 = str1[0:3:1]
# print(str2)
# # 截取字符串最后三位的字符
# str2 = str1[-1:-4:-1]
# print(str2)
# # 截取字符串的全部字符
# str2 = str1[::]
# print(str2)
# # 截取字符串的第七个字符到结尾
# str2 = str1[6::1]
# print(str2)
# # 截取字符串的第一位到倒数第三位之间的字符
# str2 = str1[0:-3:1]
# print(str2)
# # 截取字符串的第三个字符
# str2 = str1[2:3:1]
# print(str2)
# # 截取字符串的倒数第一个字符
# str2 = str1[-1:-2:-1]
# print(str2)
# # 截取与原字符串顺序相反的字符串
# str2 = str1[::-1]
# print(str2)

#  6.	倒序遍历字符串”helloworld” (用三种方法实现)

# a = "helloworld"
# b = a[::-1]
# i = 0
# #  第一种
# for c in b:
#     print(c)
#  第二种
# while i <len(b):
#     print(b[i])
#     i += 1
#  第三种
# d = len(a)-1
# while d>=0:
#     print(a[d])
#     d -= 1


#  7.	请将s = 'aAsmr3idd4bgs7Dlsf9eAF'，字符串的数字取出，并输出成一个新的字符串

# s = "aAsmr3idd4bgs7Dlsf9eAF"
# s_1=s.split(s)
# print(s_1)
# s_2 = ""
# for a in s:
#
#     if a.isdecimal()==True:
#         print(type(a))
#         s_2.a(a)
#         print(s_2)

