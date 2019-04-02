from unittest import TestCase, mock
from exercicio_08 import filter_pizzas



class TestFilterPizzas(TestCase):

    @mock.patch('exercicio_08.sabores_de_pizza', return_value=[('Queijunto', 14.90), ('Portuguesa', 20.90), ('Baiana', 30.23)])
    def test_filtes_pizzas_deve_retornar_lista_vazia_com_pizzas_de_valor_acima_de_1(self, mocked):
        esperado = []

        self.assertEqual(filter_pizzas(1, mocked()), esperado)


    @mock.patch('exercicio_08.sabores_de_pizza', return_value=[('Queijunto', 14.90), ('Portuguesa', 20.90), ('Baiana', 30.23)])
    def test_filter_pizzas_deve_retornar_lista_com_apenas_pizzas_de_valor_abaixo_de_15(self, mocked):
        esperado = [('Queijunto', 14.90)]

        self.assertEqual(filter_pizzas(15.00, mocked()), esperado)

    def test_filter_pizzas_deve_retornar_lista_vazia_com_entrada_vazia(self):
        esperado = []

        self.assertEqual(filter_pizzas(10.00, [()]), esperado)