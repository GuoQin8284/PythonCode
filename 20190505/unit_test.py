import unittest
def myadd(a,b):
    return a+b
class TestUnit(unittest.TestCase):
    def test_myadd1(self):
        print(myadd(1,2))
    def test_myadd2(self):
        print(myadd(3,4))
