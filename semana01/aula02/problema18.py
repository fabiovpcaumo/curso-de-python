def isMultiploDe3(numero):
    if numero % 3 == 0:
        return "queijo"
    return numero


def isMultiploDe5(numero):
    if numero % 5 == 0:
        return "goiabada"
    return numero


def isMultiploDe3e5(numero):
    if numero % 5 == 0 and numero % 3 == 0:
        return 'romeu e julieta'
    else:
        return numero


Funcoes = [isMultiploDe3e5, isMultiploDe5, isMultiploDe3]


def aplica_em_lotes(func, valor):
    if valor % 3 == 0 and valor % 5 == 0:
        return func[0](valor)
    elif valor % 5 == 0:
        return func[1](valor)
    elif valor % 3 == 0:
        return func[2](valor)
    else:
        return valor


print(aplica_em_lotes(Funcoes, 3))
print(aplica_em_lotes(Funcoes, 5))
print(aplica_em_lotes(Funcoes, 15))
print(aplica_em_lotes(Funcoes, 19))

