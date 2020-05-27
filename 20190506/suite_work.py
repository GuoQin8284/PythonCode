import unittest
import time

from parameterized.parameterized import parameterized

import work
from HTMLTestRunner import HTMLTestRunner
from work import Test_unit

suite = unittest.TestSuite()
unittest.TestLoader().discover("D:/python code/20190505/模板代码/day4","lianxi*.py")
# suite.addTest(Test_unit("test_01"))
# suite.addTest(Test_unit("test_02"))

with open("./report/work_report{}.html".format(time.strftime("%Y%m%d%H%M%S")),"wb") as s:
    HTMLTestRunner(s,title="tpshopsuite测试").run(suite)