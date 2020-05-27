# 带入random模块,生成1-100间所有整数的随机列表(列表中的数字不重复,长度为100)
import random
list_1=[]
i = 1
while i<=100:
    b=random.randint(1,100)
    if list_1.count(b)==0:
        list_1.append(b)
        i += 1
        if len(list_1)==100:
            break
    else:
        continue

print(list_1)