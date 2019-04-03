"""
Ex. 1: Classe Bola: Crie uma classe que modele uma bola:
Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
"""

class Bola:

    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    
    def mostraCor(self):
        print(f'Cor da bola: {self.cor}')
    
    def trocaCor(self, cor):
        self.cor = cor
        print("A cor da bola foi trocada.")
        self.mostraCor()


if __name__ == "__main__":
    bola = Bola("Branca", "5m", "Metal")
    bola.mostraCor()
    bola.trocaCor("Verde")