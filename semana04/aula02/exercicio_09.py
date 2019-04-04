"""
Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:
Possua uma classe chamada Ponto, com os atributos x e y.
Possua uma classe chamada Retangulo, com os atributos largura e altura.
Possua uma função para imprimir os valores da classe Ponto
Possua uma função para encontrar o centro de um Retângulo.
Você deve criar alguns objetos da classe Retangulo.
Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, que deve ser um objeto da classe Ponto.
A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique os valores de x e y para o centro do objeto.
O valor do centro do objeto deve ser mostrado na tela
Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.
"""

class Ponto:


    def __init__(self, x, y):
        self.x = x
        self.y = y


    def retorna_ponto(self):
        return f'Ponto {self.x}, {self.y}'


class Retangulo:
    
    
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.vertice_de_partida = Ponto(0, 0)


    def centro_retangulo(self):
        centro = Ponto(self.largura/2, self.altura/2)
        # print(f'Centro do retangulo: {self.largura/2}, {self.altura/2}')
        print(f'Centro do retangulo: {centro.retorna_ponto()}')

    def set_tamanho(self, altura_, largura_):
        self.largura = largura_
        self.altura = altura_
        

if __name__ == "__main__":
    r1 = Retangulo(10, 10)
    r2 = Retangulo(20, 10)
    r3 = Retangulo(3, 2)
    r4 = Retangulo(7, 8)
    p1 = Ponto(0, 0)

    altura_r = int(input("Insira um número inteiro para a altura do retângulo: "))
    largura_r = int(input("Insira um número inteiro para a largura do retângulo: "))
    
    r = Retangulo(altura_r, largura_r)

    while True:
        r.centro_retangulo()
        
        choice = input("Deseja alterar os lados do retangulo? (S/N) ")

        if choice.lower() == 's':
            altura_ = int(input("Insira a nova altura do retangulo: "))
            largura_ = int(input("Insira a nova largura do retangulo: "))
            r.set_tamanho(altura_, largura_)
        else:
            print("Encerrando o software")
            break
