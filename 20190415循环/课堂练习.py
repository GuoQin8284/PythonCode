#   判断两个整数之间范围内 奇数
# a = int(input('第一位正整数：'))
# b = int(input('第二位正整数：'))
# if a > 0 and b > 0 :
#     while a - b:
#         while a > b:
#             if a % 2:
#                 print('%d \t' % a, end="")
#                 a -= 1
#             else:
#                 a -= 1
#         while a < b:
#             if a % 2:
#                 print('%d \t' % a, end="")
#                 a += 1
#             else:
#                 a += 1
#     print('')
# else:
#     print('请输入正整数')

#  2.	判断一个正整数有多少位，例如375有3位， 1000有4位， 0有1位

#
# a = int(input('请输入自然数:'))
# if a>=0:
#     i = 0
#     b = 1
#     while b != 0:
#         b = a // 10
#         a //= 10
#         i += 1
#     print(i)
# else:
#     print('请输入自然数')


#  3. 统计一个自然数的二进制表示形式中有多少个 1

# a = int(input('请输入自然数'))
# if a>=0:
#     i = 0
#     b = 1
#     while a != 0:
#         b = a % 2
#         a //= 2
#         if b :
#             i += 1
#     print(i)
# else:
#     print('请输入自然数')


#   4. 判断1-100的数字里有多少个9
# i = 0
# b = 9
# while 0< b <= 100:
#     if b < 89:
#         b += 10
#         i += 1
#     else:
#         b += 1
#         i += 1
# print(i)


#  1.	循环输入若干个数，当输入0时，停止输入。
# a = int(input('请输入数字：'))
# b = a
# while a != 0 :
#     a = int(input('请输入数字：'))
#     if a > b :
#         b = a
#     elif a == 0:
#         print('%d'%b)
#         break


#  2.	计算1-10的累加和时不把5计算在内。

# i = 1
# a = 0
# while i<=10:
#     if i == 5:
#         i += 1
#         continue
#     a = a + i
#     i += 1
# print(a)


#  1.	定义一个函数is_even(n)，判断数据n是否为偶数，若是偶数，函数的返回值为True，若不是偶数，则函数的返回值为False


def is_enen():
    n=int(input('请输入：'))
    if n % 2:
        print('False')
    else:
        print('True')
        return n
if is_enen() > 5:
    print('%d'% is_enen())






