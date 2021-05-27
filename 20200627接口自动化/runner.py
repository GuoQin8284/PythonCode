import os
import time
import unittest

import config
from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestLoader().discover(start_dir=config.path+os.sep+"case", pattern="test_*.py")

with open(file=config.path+os.sep+"report"+os.sep+"{}登录接口测试报告.html".format(time.strftime("%Y-%m-%d %H_%M_%S")), mode="wb") as f:
    runner = HTMLTestRunner(stream=f, description="https协议")
    runner.run(suite)