import threading
from threading import Thread
import time


class Work01(Thread):

    def __init__(self, num):
        super().__init__()
        self.num = num

    def dance(self, num):
        for i in range(num):
            print("dance"+str(i))
            time.sleep(1)

    def run(self):
        self.dance(self.num)

class Work02(Thread):

    # 通过init方法将函数的参数传进去
    def __init__(self, num):
        super().__init__()
        self.num = num

    def sing(self, num):
        for i in range(num):
            print("sing" + str(i))
            time.sleep(1)

    def run(self):
        self.sing(self.num)

t1 = Work01(5)
t2 = Work02(5)

t1.start()
t2.start()