# def sum():
#     a_1 = 1
#     b_2 = 2
#     print(a_1,b_2)
#     return a_1,b_2
# a = 10
# b = 20
# b_2,a_1=sum()
# # print("相加和为%d"% sum())
# print("a_1=%d \t b_2=%d"%(a_1,b_2))
# print(a,b)
# import random
# b = []
# def set_extreme():
#     for list_str in range(10):
#         a = random.randint(0, 100)
#         b.append(a)
#     print(b)
#     a_1 = b.index(max(b))
#     b_1 = b.index(min(b))
#     print(a_1)
#     print(b_1)
#     y_1 = b[0]
#     y_2 = b[1]
#     b[0],b[a_1]=max(b),y_1
#     b[1],b[b_1]=min(b),y_2
#     print(b)
# set_extreme()
# print(b)

# def print_s(s):
#     print('%s'%s)
# def print_n(n):
#     print('%d'%n)
# def print_f(f):
#     print('%f'%f)
# def p_s(f,n):
#     f(n)
# p_s(print_f,1.9)
# p_s(print_s,[1,2,3])
# p_s(print_n,1234567)


f = lambda n: n>=0
print(f(0))


