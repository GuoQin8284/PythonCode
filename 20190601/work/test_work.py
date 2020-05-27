import pytest


class Test_login():

    @pytest.mark.parametrize(("user","pwd"),[("usera","123456"),("zhangshan","zs123456"),("lisi","lisi123456")])
    def before(self):
        return