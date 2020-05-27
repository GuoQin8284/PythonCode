import unittest

from script.Search_goods import Search_test
from script.add_cart import Test_cart
from script.login_test import Test_login, data
from tools.utils import DriverUnit

# suite=unittest.TestLoader().discover(start_dir=".//script",pattern="*.py")
DriverUnit.set_quit_driver(False)
suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(Test_login))
suite.addTest(unittest.makeSuite(Search_test))
suite.addTest(unittest.makeSuite(Test_cart))

runner=unittest.TextTestRunner()
runner.run(suite)
DriverUnit.set_quit_driver(True)
DriverUnit.quit_driver()