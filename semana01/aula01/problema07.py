#f'' => string interpolada
#b'' => para ASCII

#Problema #07 - Faça um programa que receba uma string e responda se ela tem alguma vogal, se sim quais são?^
#Também diga se ela é uma frase ou não.

stringInicial = input("Digite uma string: ")
vogaisEncontradas = []

for i in stringInicial:
    if i in 'aeiou':
        vogaisEncontradas.append(i)

if stringInicial.count(' '):
    print("É uma frase!")

if len(vogaisEncontradas) > 0:
    print("Existem vogais na string.\nVogais: {}".format(set(vogaisEncontradas)))