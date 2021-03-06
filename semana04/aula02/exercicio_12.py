"""
Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria, 
com a diferença de que se adicione um atributo taxaJuros. 
Forneça um construtor que configure tanto o saldo inicial como a taxa de juros. 
Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta. 
Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%. 
Depois aplique o método adicioneJuros() cinco vezes e imprime o saldo resultante.
"""
from exercicio_05 import ContaCorrente

class ContaInvestimento(ContaCorrente):

    def __init__(self, saldo, taxa_juros):
        self.saldo = saldo
        self.taxa_juros = taxa_juros/100
    
    def adicionar_juros(self, meses):
        for i in range(0, meses):
            self.saldo += self.saldo * self.taxa_juros
        return self.saldo
        
