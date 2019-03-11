#Escreva um programa que leia 5 números e retorne o maior

numeros = []
while len(numeros) < 5:
    numeros.append(int(input("Digite um número: ")))
    
print("O valor máximo é: {}".format(max(numeros)))
