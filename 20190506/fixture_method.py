import unittest

import time

class Test_method(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("start time:", time.time())
    @classmethod
    def tearDownClass(cls):
        print("end time:", time.time())
    def test_01(self):
        print("test_01")
    def test_02(self):
        print("test_02")