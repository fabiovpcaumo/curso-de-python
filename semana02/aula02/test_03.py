from unittest import TestCase, main
from collections import Counter

def frequencia(texto):
    #Verifica se o texto é do tipo str
    #Se não, raise TypeError
    return Counter(texto)


class TestFrequencia(TestCase):
    
    # def setUp():
    #     ...
    
    # def tearDown():
    #     ...

    # nome = "matheus"
    # print(self.nome)

    def test_contagem_deve_ser_b1_a3_t2_com_batata(self):
        entrada = 'batata'
        esperado = {'b': 1, 'a' : 3, 't': 2}
        # print(entrada, esperado)
        self.assertEqual(frequencia(entrada), esperado)

# if __name__ == "__main__":
#     main()
    
    
