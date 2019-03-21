from unittest import TestCase, main

def transforma_em_lista(frase):
    return list(frase.split(" "))


class TestTransformaEmLista(TestCase):


    def test_deve_retornar_lista_python_e_foda_com_string(self):
        esperado = ['Python', 'é', 'foda']
        self.assertEqual(transforma_em_lista("Python é foda"), esperado)


if __name__ == "__main__":
    main()