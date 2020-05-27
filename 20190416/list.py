# ls = [1,3,4,4,5,6,6,7]
# print(ls.index(4))
# print(ls[5])
# i = 0
# a = 0
# while i<100:
#     a += 1
#     i += 1
#     ls.append(a)
# print(ls)
#
import random
ls = []
i = 1
while i<=5:
    a = random.randint(1, 100)
    ls.append(a)
    i += 1
print(ls)
b = 0
for c in ls:
    b = b + c
print(b)
# for a in range(len(ls)):
#     b = b + ls[a]
# print(b)
# print(ls)
#
# n = int(input('请输入待删除的值：'))
# if ls.count(n):
#     ls.remove(n)
# print(ls)
# suo = ls.index(n)
# ls.pop(suo)
# print(ls)

# a = '112'
# b = len(a)
# print(b)


