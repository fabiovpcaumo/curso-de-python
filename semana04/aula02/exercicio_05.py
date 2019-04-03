"""
Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. 
A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. 
Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero 
e os demais atributos são obrigatórios.
"""

class ContaCorrente:


    def __init__(self, numero_conta, nome_correntista, saldo = 0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo


    def alterar_nome(self, novo_nome):
        self.nome_correntista = novo_nome


    def deposito(self, valor):
        self.saldo += valor


    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f'Foram sacados R$ {valor}')
        else:
            print("Nâo é possível sacar pois você não tem dinheiro")


if __name__ == "__main__":
    cc = ContaCorrente('123', 'fabio')
    cc.alterar_nome('aula02')
    cc.saque(1)