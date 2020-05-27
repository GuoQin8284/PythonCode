"""
封装一个函数(无参，有返回值)：
a.如果不是数字：则直接返回“不是数字，请重新输入”
b.判断用户输入是否是数字，
      如果是数字：则继续判断,输入数字是否是9的倍数
I.如果是，返回结果“是”，
II.否则返回结果“否
"""
def num_1():
    a = input("输入数字：")
    if a.isdecimal()==False:
        return "不是数字，请重新输入"
    else:
        if int(a)%9==0:
            return "是"
        else:
            return "否"
print(num_1())