from unittest import TestCase, mock
import exp

class TestExp(TestCase):
    def test_input_indireto_soma(self):
        with mock.patch('exp.soma') as spy:
            exp(1, 2, 3)
        
        spy.assert_called_with(1, 2)

