import pytest



@pytest.fixture(params=[1,2,3])
def before(request):
    return request.param

class Test_para():

    # @pytest.mark.parametrize(("a","b"),[(1,2),(4,5)])
    # @pytest.mark.usefixtures("before")

    def test_01(self,before):
        print("before:%d"%before)
