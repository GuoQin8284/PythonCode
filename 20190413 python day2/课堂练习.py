# y = int(input('enter_year:'))
# m = int(input('enter_month:'))
# d = int(input('enter_day:'))
# print('%d年%02d月%d日,happy' % (y,m,d))

# a = 182507
# b = 33
# print('%X\t%X'%(a,b))

# a = int(input('Enter item number:'))
# b = float(input('Enter unit price:')
# print (('Item \t Unit Price \t Purchase Date'),('\n%d \t %.2f \t %s'%(a,b,c)))

# a = int(input("输入一个正整数："))
# b = a % 2
# if b==0:
#     print('该正整数为偶数')
# else:
#     print('该正整数为奇数')

# a = input("请输入第一个值：")
# b = input("请输入第二个值：")
# print(a+b)

a = int(input('请输入a值'))
b = int(input('请输入b值'))
c = int(input('请输入c值'))
if a >  b :
    if b > c:
        print('最大值为：a\n最小值为：c')
    elif a>c:
        print('最大值为：a\n最小值为：b')
    else:
        print('最大值为：c\n最小值为：b')
elif b<c:
    print('最大值为：c\n最小值为：a')
elif a>c:
    print('最大值为：b\n最小值为：c')
else:
    print('最大值为：b\n最小值为：a')


# sc = int(input('Enter numerical grade:'))
# if 0<= sc <= 100:
#     if sc <= 59:
#         print('Letter grade:F')
#     elif sc <= 69:
#         print('Letter grade:D')
#     elif sc <= 79:
#         print('Letter grade:C')
#     elif sc <= 89:
#         print('Letter grade:B')
#     elif sc <=100:
#         print('Letter grade:A')
# else:
#     print('成绩有误')

# a = int(input('a：'))
# b = int(input('b：'))
# if a != b :
#     if a>b:
#         print('a>b')
#     else:
#         print('a<b')
# else:
#     print('a=b')


# a = "Life is short,you need python\n"
# print(a*5)

# s1 = 'hello'
# s2 = 'world'
# print(s2+s2)


# a = input('Enter zone number:')
# b = input('Enter phone number:')
# print('You entered %s.%s' % (a,b))