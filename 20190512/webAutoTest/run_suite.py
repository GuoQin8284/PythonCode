# 测试套件
import unittest

from script.cart_case import TestCart




# 添加用例
suite=unittest.TestSuite()
    # suite.addTest(TestCart("test_cart"))
suite.addTest(unittest.makeSuite(TestCart))

# 关闭 退出驱动开关
# 运行
runner=unittest.TextTestRunner()
runner.run(suite)

# 打开 退出驱动开关
# 退出驱动
