import random
a = []
for n in range(10):
    a.append(random.randint(1,10))
print(a)
b = int(input('输入值：'))
start = 0
c =[]
for i in range(a.count(b)):
    d=a.index(b,start)
    c .append(d)
    start = d+1
print(c)

