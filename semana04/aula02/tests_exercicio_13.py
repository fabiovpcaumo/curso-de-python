from unittest import TestCase
from exercicio_13 import Funcionario

class TestFuncionario(TestCase):

    def setUp(self):
        self.f = Funcionario("Fabio", 25000.00)

    def tearDown(self):
        del(self.f)

    def test_aumenta_salario_deve_retornar_27500_com_25000_e_10_porcento(self):
        esperado = 27500.00
        self.assertEqual(self.f.aumenta_salario(10), esperado)

    def test_aumenta_salario_deve_retornar_25000_com_25000_e_0_porcento(self):
        esperado = 25000.00
        self.assertEqual(self.f.aumenta_salario(0), esperado)
