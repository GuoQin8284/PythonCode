import pytest


class TestAddContact():

    # 参数化修饰器
    @pytest.mark.parametrize(("name","phone"),[("zhangsan","15549080517"),("lisi","1549786212"),("wangwu","12351351")])
    def test_addContact(self,name,phone):
        print(name,phone)