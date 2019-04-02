def soma_2(numero):
    return numero + 2


def subtrai_2(numero):
    return numero - 2


def twice(f, val):
    return f(f(val))


print(twice(soma_2, 2))
print(twice(subtrai_2, 2))
