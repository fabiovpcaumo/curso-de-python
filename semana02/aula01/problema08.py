from problema03 import Calc
from exp import exp, expexp
from unittest import TestCase, main, mock

calculadora = Calc()
 
class TestExpExp(TestCase):

    dummy = 0
    def test_expexp_deve_retornar_5_com_3_2_1(self):
        print("\n[TESTE] Expressão deve resultar 5: ")        
        esperado = 5
        self.assertEqual(expexp(3, 2, 1), esperado)


    def test_exp_deve_retornar_4_com_3_2_1(self):
        print("\n[TESTE] Expressão deve resultar 4: ")
        esperado = 4
        self.assertEqual(exp(3, 2, 1), esperado)


    def test_exp_deve_retornar_4_2_1_com_exp_3_2_1_2_1(self):
        print("\n[TESTE] Expressão deve resultar (4, 2, 1): ")
        esperado = (4, 2, 1)
        self.assertEqual((exp(3, 2, 1), 2, 1), esperado)

    def test_exp_deve_retornar_1_com__1_1_dummy(self):
        print("\n[TESTE] Expressão deve resultar em 1, utilizando Dummy (0) em y, z")
        esperado = 1
        self.assertEqual(expexp(1, self.dummy, self.dummy), 1)

