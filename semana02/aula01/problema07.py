from unittest import TestCase, main
from exp import exp

class TestExp(TestCase):
   
    def test_expressao_deve_ser_3_com_2_3_e_2(self):
        print("[TESTE] Expressão deve resultar 3: ")
        self.assertEqual(exp(2, 3, 2), 3)

    def test_expressao_deve_ser_menos1_com_3_3_e_7(self):
        print("[TESTE] Expressão deve resultar -1: ")
        self.assertEqual(exp(3,3,7), -1)

    def test_expressao_deve_retornar_Type_Error_se_entrada_nao_for_numero(self):
        print("[TESTE] Expressão deve retornar Type Error: ")
        self.assertRaises(TypeError("Foram inseridos na função argumentos que não são números."), exp('a', 3, 2))