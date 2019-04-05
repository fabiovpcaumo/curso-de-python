"""
Classe Bichinho Virtual:Crie uma classe que modele um Tamagochi (Bichinho Eletrônico):
Atributos: Nome, Fome, Tédio e Idade b. Métodos: Alterar Nome, Fome, Tédio e Idade; 
Retornar Nome, Fome, Tédio e Idade Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso Tamagochi, 
este humor é uma combinação entre os atributos Fome e Tédio, ou seja, um campo calculado, então não devemos criar um atributo para armazenar 
esta informação por que ela pode ser calculada a qualquer momento.
"""
from foods import comidas
from moods import humores

class Tamagochi:
    
    humor = ""
    
    def __init__(self, nome: str, idade: int, fator_fome: int = 20, fator_tedio: int  = 30, saciedade: int = 50, diversao: int = 50):
        self.nome = nome
        self.saciedade = saciedade
        self.diversao = diversao
        self.idade = idade
        self.calcular_humor()               #Dá um humor inicial ao Tamagochi com base na sua saciedade e diversão
        self.comandos = {
            0: self.alimentar,              #Invoca a rotina de alimentação do Tamagochi
            1: self.brincar,                #Invoca a rotina de brincar com o Tamagochi
            2: self.__str__,                #Invoca o método __str__ para printar os valores do Tamagochi

        }
        self.fator_fome = fator_fome        #Indica quanto de fome o Tamagochi sente por hora (redução de saciedade)
        self.fator_tedio = fator_tedio      #Indica quanto tédio o Tamagochi sente por hora (redução de diversão)
        

    def opcoes(self, escolha: int):
        """ Recebe uma escolha do usuário para executar uma das ações do Tamagochi.
        
        Arguments:
            escolha {[int]} -- [A escolha realizada pelo usuário, validada entre as opções possíveis.]
        
        Returns:
            [method] -- [Um dos métodos em self.comandos, correspondente ao número inserido pelo usuário.]
        """

        if escolha in range(0, len(self.comandos)):
            return self.comandos.get(escolha)()
        print("Opção inválida, tente novamente.")

    
    def brincar(self):
        """
        Rotina de brincadeira do Tamagochi.
        Invoca os métodos alterar_diversao e alterar_saciedade, utilizando o tempo de brincadeira
        inserido pelo usuário do Tamagochi.
        """

        tempo = float(input(f'Por quanto tempo irá brincar com {self.nome}? (i.e: 0.5 para meia hora)'))
        print(f'Brincando com {self.nome} durante {tempo}h.')
        self.alterar_diversao(self.fator_tedio * tempo)
        self.alterar_saciedade(-(self.fator_fome * tempo))


    def alimentar(self):
        """
        Recebe uma entrada do usuário e alimenta o Tamagochi com a comida correspondente.
        O valor que cada comida aumenta na Saciedade é exibido antes da escolha do usuário,
        e é definido em foods.comidas.
        """

        for comida in comidas:
            print(f'[{comida}] aumenta em {comidas.get(comida)} pontos.')

        escolha_ = input(f'O que irá dar para {self.nome} comer? ')

        if escolha_.lower() in comidas:
            self.alterar_saciedade(comidas.get(escolha_))
        else:
            print("\n\nValor inválido, tente novamente.\n")
            self.alimentar()


    def alterar_nome(self, nome: str):
        """Altera o nome do Tamagochi.
        
        Arguments:
            nome {[str]} -- [O novo nome para o Tamagochi.]
        """

        print(f"\nAlterando nome de {self.nome} para {nome}")
        self.nome = nome


    def alterar_saciedade(self, valor: int):
        """Altera o nível de saciedade do Tamagochi.
        
        Arguments:
            valor {int} -- [O valor a adicionar no nível de saciedade atual do Tamagochi.]
        """

        print(f"\nAlterando saciedade de {self.nome} de {self.saciedade} para {self.saciedade + valor}")
        self.saciedade += valor

        if self.saciedade >= 100:
            self.saciedade = 100
        elif self.saciedade <= 0:
            self.saciedade = 0


    def alterar_diversao(self, valor: int):
        """Altera o nível de diversão do Tamagochi.
        
        Arguments:
            valor {[int]} -- [O valor a adicionar no nível de diversão atual do Tamagochi.]
        """

        print(f"\nAlterando diversão de {self.nome} de {self.diversao} para {self.diversao + valor}")
        self.diversao += valor

        if self.diversao >= 100:
            self.diversao = 100
        elif self.diversao <= 0:
            self.diversao = 0


    def alterar_idade(self, idade: int):
        """Altera a idade do Tamagochi.
        
        Arguments:
            idade {[int]} -- [A nova idade do Tamagochi.]
        """

        self.idade = idade
        self.__str__()


    def calcular_humor(self):
        """
        Calcula o humor atual do Tamagochi, com base no dicionário humoers em moods.

        """

        coeficiente_fome = 0
        coeficiente_tedio = 0
        humor = ""
        for i in range(0, 110, 10):
            if self.saciedade == 0:
                coeficiente_fome = 0
            elif self.saciedade <= i:
                coeficiente_fome = self.saciedade / i
            
            if self.diversao == 0:
                coeficiente_tedio = 0
            elif self.diversao <= i:
                coeficiente_tedio = self.diversao / i

        coeficiente_humor = (self.saciedade * coeficiente_fome + self.diversao * coeficiente_tedio)/2

        for i in humores:
            if coeficiente_humor >= humores[i]:
                humor = i

        print(f'O humor do Tamagochi é: {humor}, com {coeficiente_humor} pontos')
        self.humor = humor


    def __str__(self):
        print(f'Tamagochi {self.nome} | Saciedade: {self.saciedade} | Diversão: {self.diversao} | Idade: {self.idade}, Humor: {self.humor}')

