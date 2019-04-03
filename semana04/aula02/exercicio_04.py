"""
Classe Pessoa: Crie uma classe que modele uma pessoa:
Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. 
Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
"""


class Pessoa:
    
    
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        print(f'Envelhecendo {self.nome} em {anos} anos.')
        
        # Checar idade e aumentar 0.5 pra cada ano antes dos 21
        if self.idade < 21:
            if self.idade + anos <= 21:
                self.engordar(anos * 0.5)
            elif self.idade + anos > 21:
                self.engordar((21 - self.idade) * 0.5)

        self.idade += anos
        print(pessoa)
    
    def engordar(self, quilos):
        print(f'Engordando {self.nome} em {quilos} quilos.')
        self.peso += quilos
        print(pessoa)


    def emagrecer(self, quilos):
        print(f'Emagrecendo {self.nome} em {quilos} quilos.')
        self.peso -= quilos
        print(pessoa)
    
    def crescer(self, centimetros):
        print(f'Crescendo {self.nome} em {centimetros} centimetros.')
        self.altura += centimetros
        print(pessoa)

    def __repr__(self):
        return f'Pessoa - Nome: {self.nome}, Idade: {self.idade}, Peso: {self.peso}, Altura: {self.altura}'


if __name__ == "__main__":
    pessoa = Pessoa("Fabio", 16, 58, 1.79)
    print(pessoa)

    pessoa.emagrecer(2)
    pessoa.envelhecer(6)
    pessoa.crescer(0.39)