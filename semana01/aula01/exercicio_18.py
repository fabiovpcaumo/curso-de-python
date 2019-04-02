def calculaQuartil(lista, p):
    p_index = int(p * len(lista))
    #print(sorted(lista))
    #print(p_index)
    return sorted(lista)[p_index]

print(calculaQuartil([1, 94, 5, 34, 27, 81, 52, 53, 68, 32], 0.98))