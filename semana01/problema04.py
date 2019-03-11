#Faça um programa que peça 2 números inteiros e um número real.
#Calcule e mostre:
#O produto do dobro do primeiro com metade do segundo
#A soma do triplo do primeiro com o terceiro
#O terceiro elevado ao cubo

numero1 = int(input("[1] Digite um número inteiro: "))
numero2 = int(input("[2] Digite outro número inteiro: "))
numero3 = float(input("[3] Digite um número real: "))

produto1 = (numero1 * 2) + (numero2//2)
produto2 = (numero1 * 3) + numero3
produto3 = (numero3**3)

print(produto1)
print(produto2)
print(produto3)