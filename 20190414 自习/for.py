# for a in [1,2,3,4,'aa'] :
#     print(a)

# for b in [1,3,4,5,5,6]:
#     for a in range(20):
#         print(a)


# for a in range(20):
#     print(a,'hello')

#
# while True :
#     print('hello')


# i = 0
# while i <= 2 :
#     i = i+1
#     print('hello word \t %d' % i)
# print('%d' % i)

# i=1
# b=0
# while i <=100:
#     a = i%5
#     if a==0:
#         b += i
#         i +=1
#     else:
#         i = i + 1
#         continue
# print(b)


# a = 1
# while a<10:
#     b=1
#     while b<=a:
#         c = a * b
#         print('%02d * %02d = %02d \t' % (a,b,c) ,end="")
#         b += 1
#     a += 1
#     print ('')
#
# row = 5
# while row >= 1:
#     col = 1
#     while col <= row:
#         print('*',end = "")
#         col += 1
#     print('')
#     row = row - 1


def sum():
    a = input('a:')
    b = input('b:')
    c = a + b
    print('%x = %x + %x ' % (c,a,b))
sum()



