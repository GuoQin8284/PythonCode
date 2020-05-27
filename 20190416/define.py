# def sun (a,b) :
#     c = a + b
#     return print('两值之和分别为：%d'% c)
# i = 1
# while i<=3:
#     a = int(input('第一个值：'))
#     b = int(input('第二个值：'))
#     sun(a,b)
#     i += 1

def num(a):
    if a%2:
        return True
    else:
        return False
i = 1
while i<=5:
    a = int(input('输入值'))
    print(num(a))
    i += 1




# def test1():
#     print('ha '*10,end=(''))
# def test2():
#     print("+"*50)
#     i = 1
#     while i <=10 :
#         print("+"," "*46,"+")
#         if i == 6 :
#             print(("+"),"\t" * 2,test1(),"\t" * 2, "+" )
#         i += 1
#     print('+'*50)
# test2()

def print_line(d,r,l):
    i = 1
    while i <= l:
        print(d * r)
        i += 1
print_line('&',50,10)
