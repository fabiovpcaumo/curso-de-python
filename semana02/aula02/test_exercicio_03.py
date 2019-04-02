from exercicio_03 import contador
from unittest import TestCase, main
from collections import Counter
class TestContadorDeFrequencia(TestCase):
    
    def test_fabio_deve_retornar_f1_a1_b1_i1_o1(self):
        self.assertEqual(contador("fabio"), {"f" : 1, "a": 1, "b" : 1, "i" : 1, "o": 1})

    def test_123asd_deve_retornar_algo(self):
        with self.assertRaises(TypeError) as exc:
            contador(123)                               # Recebendo números ao invés de strings
            self.assertEqual(exc.expected, TypeError)
        
    def test_deve_retornar_algo(self):
        
        esperado = Counter()
        self.assertEqual(contador(''), esperado)
    