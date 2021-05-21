# 开发人员： 曾祥茂
# 日期： 2021/03/31
def setup_module():
    print("资源准备：setup module")


def teardown_module():
    print("资源销毁：teardown module")

def test_case1():
    print("case1")


def setup_function():
    print("资源准备：setup function")


def teardown_function():
    print("资源销毁：teardown function")


class TestDemo():
#每个类里面的前后
    def setup_class(self):
        print("TestDemo setup_class")


    def teardown_class(self):
        print("TestDemo teardown_class")
#每个类里面的方法前后
    def test_setup(self):
        print("TestDemo setup")


    def test_teardown(self):
        print("TestDemo teardown")


    def test_demo1(self):
        print("test demo1")


    def test_demo2(self):
        print("test demo1")