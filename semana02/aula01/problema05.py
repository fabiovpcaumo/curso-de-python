from problema03 import Calc
from unittest import TestCase, main

class TestCalculadora(TestCase):
    
    def setUp(self):
        self.c = Calc()

    def tearDown(self):
        del self.c

    def test_add_1_mais_1(self):
        input = self.c.add(1, 1)
        output_esperado = 2

        self.assertEquals(input, output_esperado)

    def test_sub_1_menos_1(self):
        input = self.c.sub(1, 1)
        output_esperado = 0

        self.assertEquals(input, output_esperado)

    def test_mult_1_vezes_1(self):
        input = self.c.mult(1, 1)
        output_esperado = 1

        self.assertEquals(input, output_esperado)

    def test_div_1_por_1(self):
        input = self.c.div(1, 1)
        output_esperado = 1
        
        self.assertEquals(input, output_esperado)