import pytest


class TestLogin():
    @pytest.mark.xfail(condition=True,reson="s")
    def test_01(self):
        print("hello01")
        assert 1

    @pytest.mark.skipif(5<6,reason=None)
    def test_02(self):
        print("hello02")
        assert 1

