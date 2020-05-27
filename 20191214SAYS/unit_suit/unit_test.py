import unittest

import time


from HTMLTestRunner import HTMLTestRunner
from case.case_login import Login

unit = unittest.TestSuite()
unit.addTest(unittest.makeSuite(Login))

with open('../report/adviser_report{}.html'.format(time.strftime("%Y%m%d-%H%M%S")),'wb') as e:
    runner=HTMLTestRunner(e,title="期刊PC端自动化测试报告",description='chrome')
    runner.run(unit)
