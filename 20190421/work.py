# #  1.	函数返回多个值：定义一个函数实现整数的四则运算calculate(num1, num2)，要求返回4个值，
# # 返回值是 + - * /的结果。函数调用后分别用1个变量和4个变量接收函数的返回值。
# def num_sum(a,b):
#     return a+b
# def num_sub(a,b):
#     return a-b
# def num_mul(a,b):
#     return a*b
# def num_dev(a,b):
#     return a/b
# # def num(a,b):
#     return num_sum(a,b),num_sub(a,b),num_mul(a,b),num_dev(a,b)
# print(num(1,2))
# a,b,c,d=num(1,2)
# print(a,b,c,d)
# 进阶要求：定义四个函数分别实现整数的加、减、乘、除运算,定义一个函数cal(func, a, b),四个参数的含义是：func：表示执行运
# 算的函数名称,a和b：执行运算的操作数,通过调用cal()函数实现算数运算
# def num_1(f,a,b):
#     return f(a,b)
# e = num_1(num_mul,10,100)
# print(e)

"""
2.	lambda表达式：定义lambda表达式并调用：
"""
# #  1). 判断一个整数是奇数还是偶数
# def ji_ou(x):
#     if lambda x:(x%2)==0:
#         print('偶数')
#     else:
#         print('奇数')
# ji_ou(10)
#  2). 实现对一个整数的乘以10操作
# x = int(input())
# c = lambda x:x*10
# print('%d'% c(x))
#  3). 实现两个整数的相加
sum=lambda a,b:a+b
print('%d'% sum(1,5))
#  3.	可变参数：编写函数，实现求多个数据的最大及最小值操作（mymax(*args)、mymin(*args)），要求：(不可调用max()、min()函数)
#  o	求若干个数据中的最大、最小值（使用可变参数实现）
def num (*args):
    a =