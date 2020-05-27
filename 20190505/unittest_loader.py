import unittest

loader = unittest.TestLoader()
sunit = unittest.TestLoader().discover(start_dir="./模板代码/day4/case",pattern="test*.py")
unittest.TextTestRunner().run(sunit)