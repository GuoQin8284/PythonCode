import unittest

from unit_test import TestMyadd
from 模板代码.day4.lianxi06_testcase_sub import TestMysub

unit = unittest.TestSuite()
unit.addTest(TestMyadd("test_myadd1"))
unit.addTest(TestMyadd("test_myadd2"))

unit.addTest(unittest.makeSuite(TestMyadd))
unit.addTest(unittest.makeSuite(TestMysub))

runner = unittest.TextTestRunner()
runner.run(unit)
