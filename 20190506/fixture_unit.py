import unittest

import time


class text_fixture_methon(unittest.TestCase):
    def setUp(self):
        print("start time:",time.time())
    def tearDown(self):
        print("end time:",time.time())
    def test_01(self):
        print("test_01")
    def test_02(self):
        print("test_02")