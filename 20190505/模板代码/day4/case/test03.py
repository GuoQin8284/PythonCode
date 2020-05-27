# 定义加法函数
import unittest

def myadd(a, b):
    return a + b

# 定义测试用例
# a.定义测试类
class TestMyadd03(unittest.TestCase):

# b.定义测试方法
    def test_myadd1(self):
        result = myadd(1,3)
        print('判断返回的结果是否符合预期',result)

    def test_myadd2(self):
        result = myadd(1,4)
        print('判断返回的结果是否符合预期',result)

if __name__ == '__main__':
    unittest.main()