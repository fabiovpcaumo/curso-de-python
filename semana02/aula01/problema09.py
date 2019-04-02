from unittest import TestCase, main, mock
from exp import exp

class TestExpSoma(TestCase):

    dummy = 0
    def test_soma_exp_indireta_deve_retornar_4_subtraindo_dummy(self):
        print("\n[TESTE] Expressão deve resultar 4 subtraindo Dummy (0): ")        
        esperado = 4
        self.assertEqual(exp(2, 2, self.dummy), esperado)

    