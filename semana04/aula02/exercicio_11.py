"""
Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:
Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
O consumo é especificado no construtor e o nível de combustível inicial é 0.
Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de uso:
meuFusca = Carro(15);           # 15 quilômetros por litro de combustível.
meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível.
meuFusca.andar(100);            # anda 100 quilômetros.
meuFusca.obterGasolina()        # Imprime o combustível que resta no tanque.
"""

class Carro:

    
    def __init__(self, consumo_combustivel):
        self.consumo_combustivel = consumo_combustivel
        self.quantidade_combustivel = 0


    def andar(self, distancia):
        if self.quantidade_combustivel - (distancia / self.consumo_combustivel) > 0:
            print(f'Andamos {distancia} km.')
            self.quantidade_combustivel -= distancia / self.consumo_combustivel
            self.obter_gasolina()
        else:
            print(f'Combustível insuficiente para continuar. Andamos alguns km.')


    def obter_gasolina(self):
        print(f'O tanque está com {self.quantidade_combustivel}L.')
    

    def adicionar_gasolina(self, quantidade):
        self.quantidade_combustivel += quantidade
        print(f'Adicionando {quantidade}L de gasolina no tanque.')
        self.obter_gasolina()


meu_fusca = Carro(15)                            # 15 quilômetros por litro de combustível.
meu_fusca.adicionar_gasolina(6.66666666667)      # abastece com 20 litros de combustível.
meu_fusca.andar(100)                             # anda 100 quilômetros.
meu_fusca.obter_gasolina()                       # Imprime o combustível que resta no tanque.