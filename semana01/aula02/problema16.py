def soma_1(n):
    # return [x+1 for x in range(n+1)]
    return n + 1


def aplica_em_lote(func, val):
    lista = []
    for numero in range(val+1):
        lista.append(func(numero))
    return lista


print(aplica_em_lote(soma_1, 5))
