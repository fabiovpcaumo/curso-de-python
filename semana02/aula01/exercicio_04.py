from unittest import TestCase
from problema03 import Calc


class TestCalculadora(TestCase):

    def setUp(self):
        print("\nNo setUp")
        self.calculadora = Calc()

    def tearDown(self):
        print("No tearDown")
        del self.calculadora

    def test_soma_deve_retornar_2_com_1_e_1(self):
        print("Testando soma")
        self.assertEqual(self.calculadora.add(1, 1), 2)

    def test_sub_deve_retornar_0_com_1_e_1(self):
        print("Testando subtração")
        self.assertEqual(self.calculadora.sub(1, 1), 0)
    
    def test_mult_deve_retornar_1_com_1_e_1(self):
        print("Testando multiplicação")
        self.assertEqual(self.calculadora.mult(1, 1), 1)
    
    def test_div_deve_retornar_1_com_1_e_1(self):
        print("Testando divisão")
        self.assertEqual(self.calculadora.div(1, 1), 1)

"""
SUTs:
- Calculadora
    - Funções de Soma, Subtração, Divisão, Multiplicação
"""
