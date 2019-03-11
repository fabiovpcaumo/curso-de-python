lista = []
novaLista = []
resultado = 0

while len(lista) < 5:
    lista.append(int(input("Insira um número na posição {}/5 da lista: ".format(len(lista)+1))))

for i in lista:
    resultado = resultado + i
    novaLista.append(resultado)
print("Lista original: {}".format(lista))
print("Lista acumulada: {}".format(novaLista))