import unittest

def add(a,b):
    result=a+b
    print(result)

class Test00(unittest.TestCase):



    def test01(self):
        add(5,8)

    def test02(self):
        add(100,1000)

if __name__=='__main__':
    unittest.main()