from itertools import combinations_with_replacement

lista = []
while len(lista) < 5:
    lista.append(int(input("Insira um número na posição {}/5 da lista: ".format(len(lista)+1))))

print([list(a) for a in combinations_with_replacement(lista, 2)])
