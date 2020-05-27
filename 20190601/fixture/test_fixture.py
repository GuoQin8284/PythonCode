import pytest

a = 3

class Test_login():

    def before(self,request):
        print("before")

    def setup(self):
        print("setup")

    @pytest.mark.skipif(condition=True,reason="hehe")
    def test_01(self):
        print("login01")

    @pytest.mark.xfail(condition=True,reason="haha")
    def test_02(self):
        print("login02")
        assert 0

    @pytest.mark.xfail(a>3, reason="haha")
    def test_03(self):
        print("login03")
        assert 0

    @pytest.mark.xfail(condition=False, reason="haha")
    def test_04(self):
        print("login04")
        assert 1

    @pytest.mark.xfail(condition=True, reason="haha")
    def test_05(self):
        print("login05")
        assert 1

    @pytest.mark.run(order=1)
    def test_06(self):
        print("login06")
        assert 0



