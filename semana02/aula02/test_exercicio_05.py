from exercicio_05 import one_function_to_rule_them_all
from unittest import TestCase, mock
from collections import Counter

stubTransformador = ''
stubContador = ''

class TestOneFunctionToFindThem(TestCase):


    def test_funcao_deve_retornar_um_tipo_collections_Counter(self):
        esperado = Counter
        self.assertEqual(type(one_function_to_rule_them_all("teste")), esperado)

    def test_funcao_deve_retornar_python_1_e_1_purin_2(self):
        esperado = {'python': 1, 'purin': 2, 'é': 1}
        self.assertEqual(one_function_to_rule_them_all("python é purin purin"), esperado)

    def test_funcao_deve_retornar_Counter_vazio_e_1_com_stub_transformador(self):
        esperado = {'': 1}
        self.assertEqual(one_function_to_rule_them_all(stubTransformador), esperado)

    def test_funcao_deve_retornar_Counter_vazio_e_1_com_stub_contador(self):
        esperado = {'': 1}
        self.assertEqual(one_function_to_rule_them_all(stubContador), esperado)

    def test_funcao_externa_deve_ser_chamada_com_palavra(self):
        with mock.patch('exercicio_05.transformador') as spy:
            one_function_to_rule_them_all('passarinho quando nasce')
        
        spy.assert_called_with('passarinho quando nasce')

    def test_funcao_interna_deve_ser_chamada_com_lista(self):
        with mock.patch('exercicio_05.contador') as spy:
            one_function_to_rule_them_all('passarinho quando nasce')
        
        spy.assert_called_with(['passarinho', 'quando', 'nasce'])