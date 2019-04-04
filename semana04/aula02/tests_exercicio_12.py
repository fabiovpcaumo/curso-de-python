from unittest import TestCase
from exercicio_12 import ContaInvestimento

class TestContaInvestimento(TestCase):

    def setUp(self):
        self.c = ContaInvestimento(100, 10)

    def tearDown(self):
        del(self.c)

    def test_adicionar_juros_deve_retornar_121_com_100_reais_e_5_meses_e_taxa_10(self):
        esperado = (161.051)
        self.assertEqual(self.c.adicionar_juros(5), esperado)

    def test_adicionar_juros_deve_retornar_100_com_100_reais_e_0_meses_e_taxa_10(self):
        esperado = (100.00)
        self.assertEqual(self.c.adicionar_juros(0), esperado)
