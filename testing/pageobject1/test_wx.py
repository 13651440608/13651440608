# 开发人员： 曾祥茂
# 日期： 2021/03/31
from testing.pageobject1.index_page import IndexPage


class TestWX:
    def setup(self):
        self.index = IndexPage()


    def test_register(self):
         assert self.index.goto_login().goto_register().register()

        # assert self.index.goto_register()
