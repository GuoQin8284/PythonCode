# i = 1
# while i <=10:
#     print('%d hahaha'% i)
#     i = i + 1


#写入5个值并输出
# i = 1
# while i<=5:
#     a=input('第%s个值：'% i )
#     print(a)
#     i=i+1

#
# i=1
# while i<=10:
#     a=i%2
#     if a != 0:
#         print('%d' % i)
#     i=i+1

# i=11
# while i<=20:
#     print(i)
#     i=i+2

# a = int(input('第一个值：'))
# b = int(input('第二个值：'))
# c = 0
# while a<=b:
#     c += a
#     a +=1
# else:
#     print("和为：%d"%c)


# i = 1
# a = 1
# while i<=10:
#     a *= i
#     i += 1
# else:
#     print('积为：%d'% a)


a = int(input('第一个值：'))
b = int(input('第二个值：'))
c = 0
while a<=b:
    if a %2== 0:
        c += a
        a += 2
    else:
        a += 1
print("偶数和为：%d"%c)





