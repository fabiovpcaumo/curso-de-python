from unittest import TestCase, main
from exp import exp

class TestExp(TestCase):
   
    def expressao_deve_ser_3_com_2_3_e_2(self):
        print("[TESTE] Expressão deve resultar 3: ")
        self.assertEqual(exp(2, 3, 2), 3)

    def expressao_deve_ser_menos1_com_3_3_e_7(self):
        print("[TESTE] Expressão deve resultar -1: ")
        self.assertEqual(exp(3,3,7), -1)

    