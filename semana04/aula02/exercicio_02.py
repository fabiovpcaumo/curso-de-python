"""
Ex.2:

Classe Quadrado: Crie uma classe que modele um quadrado:
Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""


class Quadrado:


    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado

    def mudar_tamanho(self, valor):
        self.tamanho_lado = valor
        print(f'O novo tamanho do quadrado é: {self.get_tamanho_lado()}')
    
    def get_tamanho_lado(self):
        return self.tamanho_lado
    
    def calcular_area(self):
        print(f'A área do quadrado é: {self.get_tamanho_lado() ** 2}')

if __name__ == "__main__":
    quadrado = Quadrado(2)
    print(quadrado.get_tamanho_lado())
    quadrado.calcular_area()
    quadrado.mudar_tamanho(3)
    print(quadrado.get_tamanho_lado())
    quadrado.calcular_area()