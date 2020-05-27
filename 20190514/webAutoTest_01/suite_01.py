import unittest

from script.test_login import Test_login
from script.test_search import Test_search
from units import DriverUnits

suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(Test_login))
suite.addTest(unittest.makeSuite(Test_search))
DriverUnits.set_auto_quit(False)
unittest.TextTestRunner().run(suite)
DriverUnits.set_auto_quit(True)
DriverUnits.driver_quit()