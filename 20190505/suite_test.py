import unittest

from unit_test import TestUnit

unit=unittest.TestSuite()
unit.addTest(TestUnit("test_myadd1"))
unit.addTest(TestUnit("test_myadd2"))
unit.addTest(unittest.makeSuite(TestUnit))

run = unittest.TextTestRunner()
run.run(unit)