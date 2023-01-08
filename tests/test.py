import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
       self.calc = Calculator()

    def test_adding_success(self):
        assert self.calc.adding(5, 1) == 6

    def test_subtraction_success(self):
        assert self.calc.subtraction(12, 7) == 5

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(1, 0)

    def test_multyplay_success(self):
        assert self.calc.multiply(2, 8) == 16

    def teardown (self):
        print('Выполнение метода Teardown')