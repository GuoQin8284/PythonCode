import unittest
from HTMLTestRunner import HTMLTestRunner

unit=unittest.TestLoader().discover(start_dir='./',pattern='test01.py')

report_path='./report'

with open(report_path+'/report.html','wb') as f:
    runner = HTMLTestRunner(f,title='xx自动化测试报告',description='chrome=108')
    runner.run(unit)
