lista = ['keep', 'remove', 'keep', 'remove', 'keep', 'remove', 'remove', 'remove', 'keep', 'remove', 'keep', 'keep']


def keep(instrucao):
    return instrucao != 'remove'


print(list(filter(keep, lista)))

# newList = list(filter(keep, lista))
# print(newList)
