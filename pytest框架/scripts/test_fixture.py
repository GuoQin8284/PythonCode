import pytest


class TestFixture01:

    # 这是fixture装饰器
    @pytest.fixture(scope="function", autouse=1)
    def before(self):
        print("before")

    # fix函数放在那个测试函数里面，那个函数就是执行fix函数
    def test_login01(self, before):
        print("login01")

    def test_login02(self, before):
        print("login02")


num = [1, 2, 3]


# 这是fixture装饰器，当作用域scope为class时，fixture函数要写在测试类的外面，测试脚本执行的总次数 = fixture参数化次数 x 测试脚本参数化次数
# fixture参数化时，接受的参数必须时requset，调用时需要调用.param方法，即：request.param 的形式，否则报错
@pytest.fixture(scope="function", autouse=1, params=[1, 2, 3])
def before(request):
    print("before")
    return request.param + 3


class TestFixture02:

    # fix函数放在那个测试函数里面，那个函数就是执行fix函数
    @pytest.mark.parametrize("name", ["张三", "李四"])
    def test_login01(self, before, name):
        print("fixture参数化+测试用例参数化")
        print(name, end="")
        print(before)
