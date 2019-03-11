string = input("Digite uma string: ")
seuNome = input("Digite seu nome: ")

for letra in string:
    if letra not in 'aeiou':
        print(letra)
        print(seuNome)