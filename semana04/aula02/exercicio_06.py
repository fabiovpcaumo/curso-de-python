"""
Classe TV: Faça um programa que simule um televisor criando-o como um objeto. 
O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. 
Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas."""

class TV:
    limite_canal = range(1, 501)
    limite_volume = range(1, 101)


    def __init__(self, canal, volume):
        if canal not in self.limite_canal:
            self.canal = 1
        else:
            self.canal = canal
        if volume not in self.limite_volume:
            self.volume = 1
        else:
            self.volume = volume


    def mudar_canal(self, canal):
        print(f'Mudando o canal para {canal}')
        if canal in self.limite_canal:
            self.canal = canal
        else:
            print(f'O canal {canal} não é válido. Informe um canal de 1 a 500')
        print(tv)


    def mudar_volume(self, volume):
        print(f'Mudando o volume para {volume}')
        if volume in self.limite_volume:
            self.volume = volume
        else:
            print(f'O volume {volume} não é válido. Informe um volume de 1 a 100')
        print(tv)


    def __repr__(self):
        return f'A televisão está no canal {self.canal}, com volume {self.volume}'

if __name__ == "__main__":
    tv = TV(1, 20)
    tv.mudar_canal(501)
    tv.mudar_canal(123)
    tv.mudar_volume(101)
    tv.mudar_volume(33)
    
    
    