from unittest import TestCase, mock
from problema03 import Calc
from exp import exp, expexp

class TestExp(TestCase):
    def test_input_indireto_soma(self):
        x = 1
        y = 2
        z = 3
        with mock.patch('problema03.Calc.add') as mocked_add:
            exp(x, y, z)
        
        mocked_add.assert_called_with(x, y)

    def test_input_indireto_sub(self):
        z = 3
        with mock.patch('problema03.Calc.sub') as mocked_sub:
            exp(2, 1, z)
        
        mocked_sub.assert_called_with(3, z)
    

