"""
Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:
Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
tipoCombustivel.
valorLitro
quantidadeCombustivel
Possua no mínimo esses métodos:
abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
alterarValor( ) – altera o valor do litro do combustível.
alterarCombustivel( ) – altera o tipo do combustível.
alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.
"""

class BombaDeCombustivel:
    

    def __init__(self, tipo_combustivel: str, valor_litro: int, quantidade_combustivel: int):
        self.tipo_combustivel   = tipo_combustivel   
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel


    def abastecerPorValor(self, valor_a_abastecer):
        total_litros = valor_a_abastecer/self.valor_litro
        if total_litros <= self.quantidade_combustivel: 
            print(f'Abastecidos {total_litros} com R$ {valor_a_abastecer}')
            self.alterarQuantidadeCombustivel(-total_litros)
            self.mostrarQuantidadeNaBomba()
        else:
            print(f'Foram abastecidos apenas {self.quantidade_combustivel} litros pois não há mais combustível na bomba. \
                \nTotal: R$ {self.quantidade_combustivel * self.valor_litro} \
                \nFaltaram: {total_litros - self.quantidade_combustivel}L de {self.tipo_combustivel}.')
            self.alterarQuantidadeCombustivel(-self.quantidade_combustivel)
            self.mostrarQuantidadeNaBomba()


    def abastecerPorLitro(self, quantidade_de_litros):
        valor_total = quantidade_de_litros * self.valor_litro
        if valor_total <= self.quantidade_combustivel:
            print(f'Abastecidos {quantidade_de_litros} a R$ {valor_total}')
            self.alterarQuantidadeCombustivel(-quantidade_de_litros)
            print(f'Total de combustível na bomba: {self.quantidade_combustivel}')
            self.mostrarQuantidadeNaBomba()
        else:
            print(f'Foram abastecidos apenas {self.quantidade_combustivel} litros pois não há mais combustível na bomba. \
                \nTotal: R$ {self.quantidade_combustivel * self.valor_litro} \
                \nFaltaram: {quantidade_de_litros - self.quantidade_combustivel}L de {self.tipo_combustivel}.')
            self.alterarQuantidadeCombustivel(-self.quantidade_combustivel)
            self.mostrarQuantidadeNaBomba()


    def alterarValor(self, novo_valor):
        self.valor_litro = novo_valor
    

    def alterarCombustivel(self, novo_combustivel):
        self.tipo_combustivel = novo_combustivel


    def alterarQuantidadeCombustivel(self, qtde_combustivel):
        self.quantidade_combustivel += qtde_combustivel


    def mostrarQuantidadeNaBomba(self):
        print (f'Quantidade de {self.tipo_combustivel} na bomba: {self.quantidade_combustivel}')


if __name__ == "__main__":
    b1 = BombaDeCombustivel("gasolina", 3.75, 100)
    b1.abastecerPorLitro(101)
    