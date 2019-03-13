lista = ['keep', 'remove', 'keep', 'remove', 'keep', 'remove']

def keep(instrucao):
    return instrucao != 'remove'

for i in lista:
    print(keep(i))

lista_n = filter(keep, lista)
for i in lista_n:
    print(i)