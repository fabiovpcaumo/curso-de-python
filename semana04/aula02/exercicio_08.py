"""
Classe Macaco: 
Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir(). 
Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando
o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?
"""

 
class Macaco:
    
    
    def __init__(self, nome: str, bucho: list):
        self.nome = nome
        self.bucho = bucho
    

    def comer(self, alimento):
        self.bucho.append(alimento)
        self.verBucho()
    
    def verBucho(self):
        print(f'Bucho de {self.nome}: {self.bucho}')
        print(self.bucho)
    

    def digerir(self):
        while len(self.bucho) > 0:
            print(f'Foi digerido o alimento: {self.bucho.pop(0)}')

    
if __name__ == "__main__":
    macaco1 = Macaco('maquita', [])
    macaco2 = Macaco('mococo', ['banana'])
    
    print(macaco1)
    macaco1.comer('banana')
    macaco1.comer('maçã')
    macaco1.comer(macaco2)
    macaco1.digerir()
    macaco1.verBucho()