# 编写一个函数，求1到100之间的奇数和？(5分)

def sum():
    b = 0
    for a in range(1,101)[0::2]:
        b += a
    return b
print(sum())