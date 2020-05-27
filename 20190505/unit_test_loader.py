import unittest
loader= unittest.defaultTestLoader
unit = loader.discover(start_dir="./模板代码/day4/case",pattern="test*.py")
unittest.TextTestRunner().run(unit)