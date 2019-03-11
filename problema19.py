def calculaDispersao(lista):
    #Amplitude da lista (maior valor - menor valor)
    dispersao = max(lista) - min(lista)
    return dispersao

print(calculaDispersao([1, 94, 5, 34, 27, 81, 52, 53, 68, 32]))
