import unittest
def myadd(a,b):
    return  a+b

class TestMyadd(unittest.TestCase):

    def test_myadd1(self):
        result = myadd(1,3)
        print("检查实际是否符合预期：",result)
    def test_myadd2(self):
        result = myadd(2,3)
        print("检查是否符合预期：",result)


