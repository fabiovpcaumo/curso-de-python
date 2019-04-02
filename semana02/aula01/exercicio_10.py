from unittest import TestCase, main, mock
from exp import expexp

class TestExpExpSub(TestCase):

    dummy = 0
    def test_soma_exp_indireta_deve_retornar_negativo4_subtraindo_dummy(self):
        print("\n[TESTE] Expressão deve resultar -4 somando apenas valores Dummy (0): ")        
        esperado = -4
        self.assertEqual(expexp(self.dummy, self.dummy, 2), esperado)

    