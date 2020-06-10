import pytest
class Testlogin():

    android = 8.0

    @pytest.mark.xfail(condition=True ,reason="")  #预期失败装饰器
    @pytest.mark.skipif(android <= 8.0,reason="")  #跳过测试函数装饰器
    @pytest.mark.run(order = 3)                    #控制函数执行顺序装饰器
    def test_01(self):
        print("test_01")
        assert 1

    @pytest.mark.xfail(False,reason="")
    @pytest.mark.skipif(False,reason="")
    @pytest.mark.run(order = 2)
    def test_02(self):
        print("test_02")
        assert 1
    @pytest.mark.xfail(True,reason="")
    @pytest.mark.skipif(False, reason="")
    @pytest.mark.run(order=2)
    def test_03(self):
        print("test_03")
        assert 0

    @pytest.mark.xfail(False,reason="")
    @pytest.mark.skipif(False, reason="")
    @pytest.mark.run(order=2)
    def test_04(self):
        print("test_02")
        assert 0