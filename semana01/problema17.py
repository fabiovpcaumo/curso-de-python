#from problema16 import calculaMedia

def calculaMediana(lista):
    if len(lista) % 2 == 0:
        #Caso a lista seja de tamanho par, a mediana é composta da média dos dois elementos centrais.
        #Os elementos centrais são obtidos por len(lista)//2 (meio da lista) e o número seguinte.
        #mediana = calculaMedia([lista[(len(lista)//2)], lista[(len(lista)//2)+1]])
        mediana = (lista[(len(lista)//2)] + lista[(len(lista)//2)+1])/2
    else:
        #Caso a lista seja de tamanho impar, a mediana é composta pelo elemento central.
        mediana = sorted(lista)[(len(lista)//2)]
    return mediana

print(calculaMediana([1, 9, 3, 5, 8]))
print(calculaMediana([1, 9, 3, 5, 8, 11]))