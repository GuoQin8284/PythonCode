# 定义一个加法函数  返回  和
import unittest


def mysub(a,b):
    return a-b


# 定义测试类  ---  必须继承unittest.TestCase
class TestMysub(unittest.TestCase):
    # 定义测试方法 --- 方法名必须是test开头
    def test_mysub1(self):
        # 3,1  预期  2
        result= mysub(3,1)
        print("检查实际是否符合预期:",result)


    def test_mysub2(self):
        # 3,2  预期  1
        result= mysub(3,2)
        print("检查实际是否符合预期:",result)


if __name__ == '__main__':
    unittest.main()




