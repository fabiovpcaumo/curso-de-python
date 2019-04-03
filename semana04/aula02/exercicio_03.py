"""
Ex. 3: 
Classe Retangulo: Crie uma classe que modele um retangulo:
Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. 
Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
"""

class Retangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def mudar_valor_lados(self, base, altura):
        self.base = base
        self.altura = altura
        print(f'A base e altura foram alteradas para b: {self.base} e h: {self.altura}')
    
    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return (self.base * 2) + (self.altura * 2)


if __name__ == "__main__":
    base_local = float(input("Insira a largura do local a ser calculado: "))
    altura_local = float(input("Insira o comprimento do local a ser calculado: "))
    local = Retangulo(base_local, altura_local)
    area_local = local.calcular_area()
    
    base_piso = float(input("Insira a largura do piso a ser utilizado no local: "))
    altura_piso = float(input("Insira o comprimento do piso a ser utilizado no local: "))
    piso = Retangulo(base_piso, altura_piso)
    area_piso = piso.calcular_area()

    
    # Checa se o valor da divisão é maior que o floor ( ). Se for, retorna o valor arredondado para baixo + 1.
    qtde_pisos_necessarios = (area_local // area_piso) + 1 if (area_local / area_piso) > (area_local // area_piso) else area_local / area_piso
    qtde_rodape = local.calcular_perimetro()

    print(f'Quantidade de pisos necesśarios para cobrir todo o local (Quantidade arredondada): {qtde_pisos_necessarios}')
    print(f'Quantidade de rodapé para circundar todo o local: {qtde_rodape}')

    

    