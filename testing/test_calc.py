# 开发人员： 曾祥茂
# 日期： 2021/03/31
import pytest

from pythoncode.calculator import Calculator


class TestCalc:
    def setup_class(self):
        print("计算开始")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    # def test_add(self):
    #     #calc = Calculator()
    #     result = self.calc.add(1,1)
    #     assert result == 2


    @pytest.mark.parametrize('a,b,expect',[
        [1,1,2],[1000,1000,2000],[0.1,0.2,0.3],[-1,-1,-2]
    ])
    def test_add1(self,a,b,expect):
        #calc = Calculator()
        result = self.calc.add(a,b)
        assert round(result,2) == expect

    @pytest.mark.parametrize('a,b,expect',[
        [1, 1, 0], [1000, 100, 900], [0.3, 0.2, 0.3], [-1, -1, 0]
    ])

    def test_sub(self,a,b,expect):
        #calc = Calculator()
        result = self.calc.sub(a,b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect', [
        [1, 1, 1], [1000, 100, 100000], [0.3, 0.1, 0.03], [-1, -1, 1]
    ])
    def test_mul(self, a, b, expect):
        # calc = Calculator()
        result = self.calc.mul(a, b)
        assert result == expect



    # 除数为0的情况下
    @pytest.mark.parametrize('a,b', [
        [1, 0], [1000, 0], [0.3,0], [-1, 0]
    ])

    def test_div1(self,a,b):
        with pytest.raises(ZeroDivisionError):
            result = self.calc.div(a,b)






    # def test_sub(self):
    #     calc = Calculator()
    #     result = calc.sub(1,1)
    #     assert result == 0
    #
    # def test_mul(self):
    #     calc = Calculator()
    #     result = calc.mul(1,1)
    #     assert result == 1
    #
    # def test_div(self):
    #     calc = Calculator()
    #     result = calc.div(1,1)
    #     assert result == 1