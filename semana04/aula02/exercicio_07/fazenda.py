from tamagochi_facade import BichinhoVirtual
from random import randrange

bichinhos = [BichinhoVirtual('Bichinho 1', '1'), BichinhoVirtual('Bichinho 2', '1'), 
            BichinhoVirtual('Bichinho 3', '1'), BichinhoVirtual('Bichinho 4', '1')]

def fazenda():
    print("Bem vindo ao bichinho virtual. \n")
    print("Brinque com seu bichinho virtual. \n")

    while True:
        print("\n\n\n------------------------------")
        print('\n0: Alimentar\n1: Brincar\n')
        escolha_ = int(input("Escolha uma opção: "))
        for bichinho in bichinhos:
            bichinho.tamagochi.calcular_humor()
            bichinho.tamagochi.opcoes(escolha_)

fazenda()