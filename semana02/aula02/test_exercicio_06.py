from unittest import TestCase
from exercicio_06 import filter_users


def stub_get_users():
    return [(101, 'Fabio', 'fabiovpcaumo@gmail.com'), (99, 'ABC', 'abcde@gmail.com'),
                                        (507, 'Jorge', 'jorgin_gatin@gmail.com')]


class TestFilterUsers(TestCase):
   

    def test_filter_users_deve_retornar_lista_vazia_com_usuario_de_id_menor_que_100(self):
        
        esperado = []
        self.assertEqual(filter_users([(100, 'Fabio', 'fabiovpcaumo@gmail.com')]), esperado)

    def test_filter_users_deve_retornar_lista_vazia_com_lista_com_tupla_vazia(self):
        
        esperado = []
        self.assertEqual(filter_users([()]), esperado)

    def test_filter_users_deve_retornar_lista_vazia_com_lista_com_varias_tuplas_vazias(self):
        
        esperado = []
        self.assertEqual(filter_users([(), (), (), (), ()]), esperado)

    def test_filter_users_deve_retornar_apenas_usuarios_com_id_maior_que_100(self):

        esperado = [(101, 'Fabio', 'fabiovpcaumo@gmail.com'), (507, 'Jorge', 'jorgin_gatin@gmail.com')]
        self.assertEqual(filter_users(stub_get_users()), esperado)