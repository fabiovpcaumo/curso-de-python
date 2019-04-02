from exercicio_04 import transformador
from unittest import TestCase

class TestTransformador(TestCase):
    

    def test_transformador_deve_retornar_lista(self):
        esperado = list
        self.assertEqual(type(transformador("teste")), esperado)

    def test_deve_retornar_lista_greatest_show_com_frase_greatest_show(self):
        esperado = ['greatest', 'show']
        self.assertEqual(transformador("greatest show"), esperado)

    def test_deve_retornar_lista_com_um_elemento_vazio(self):
        esperado = ['']
        self.assertEqual(transformador(''), esperado)
