import threading
import time


def dance(num):
    for i in range(0,num+1):
        print("dance" + str(i))
        time.sleep(1)

def sing(num):
    for i in range(0, num + 1):
        print("sing" + str(i))
        time.sleep(1)
# 创建线程,并通过args变量向函数内传递参数
t1  = threading.Thread(target=dance, args=(5,))
t2 = threading.Thread(target=sing,args=(6,))

# 启动线程
t1.start()
t2.start()

for i in range(7):
    # 获取所有线程，返回一个列表
    thread_num = threading.enumerate()
    print(thread_num)
    time.sleep(1)