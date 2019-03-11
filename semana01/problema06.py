#Faça um programa que pergunte o preço de três produtos e informa qual produto
#você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produto1 = float(input("Digite o preço do produto 1: "))
produto2 = float(input("Digite o preço do produto 2: "))
produto3 = float(input("Digite o preço do produto 3: "))
menorValor = min(produto1, produto2, produto3)

print("Menor Valor: {}".format(menorValor))