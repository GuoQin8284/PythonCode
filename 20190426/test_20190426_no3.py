# 使用while循环输出九九乘法表

i=1
while i<10:
    a =1
    while a<=i:
        b =i*a
        print("%d=%d*%d"%(b,i,a),end="\t")
        a += 1
    print("\n")
    i += 1