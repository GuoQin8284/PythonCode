import unittest

from test01 import Test00

unit=unittest.TestSuite()

# 第一种添加方法
# unit.addTest(Test00('test01'))
# unit.addTest(Test00('test02'))

# 第二种添加方法
unit.addTest(unittest.makeSuite(Test00))

runner = unittest.TextTestRunner()


runner.run(unit)