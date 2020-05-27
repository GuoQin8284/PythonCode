import unittest
from parameterized import parameterized
def myadd(a,b):
    return a + b
class duanyan(unittest.TestCase):
    # def test_myadd1(self):
    #     result = myadd(1,3)
    #     self.assertEqual(4,result)
    # def test_myadd2(self):
    #     result = myadd(1,4)
    #     self.assertIn(result,[1,2,5,32])
    # def test_myadd3(self):
    #     result = myadd(1,10)
    #     self.assertTrue(True)
    data=[(1,1,2),(2,3,5),(3,4,7)]
    @parameterized.expand(data)
    def test_myadd(self,a,b,expect):
        result = myadd(a,b)
        self.assertEqual(expect,result)
