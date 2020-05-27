import unittest

import time

from HTMLTestRunner import HTMLTestRunner
from unitest_tpshop import Test_unit1

suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(Test_unit1))
suite.addTest(Test_unit1("test_01"))
a = time.strftime("%Y%m%d%H%M%S")
with open(("./report/report{}.html".format(a)),"wb") as f:
    runner=HTMLTestRunner(f,title="tpshop自动化测试")
    runner.run(suite)