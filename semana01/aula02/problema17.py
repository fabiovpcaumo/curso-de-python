def soma_1(numero):
    return numero+1


def subtrai_1(numero):
    return numero-1


def em_lotes(func, lista_de_numeros):
    resultado = []
    for i in lista_de_numeros:
        resultado.append(func(i))
    return resultado


print(em_lotes(soma_1, [0]))
print(em_lotes(soma_1, [0, 3, 6, 9, 12]))
