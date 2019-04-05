from tamagochi import Tamagochi
from random import randrange


class BichinhoVirtual:
    
    def __init__(self, nome, idade):
        self.tamagochi = Tamagochi(nome, idade, saciedade=randrange(0, 100), diversao=randrange(0, 100))


jogo = BichinhoVirtual('Fabio', '21')
