import unittest

from itheima.API.ChannelsAPI import Channels


class Testchannels(unittest.TestCase):

    def setUp(self):

        self.login=Channels()

    def test_get_channels(self):
        self.channels=self.login.get_channels()
        print(self.channels.json())
        self.assertEqual("OK",self.channels.json().get("message"))
