from functools import reduce

lista = ['keep', 'remove', 'keep', 'remove', 'keep', 'remove']

total = len(reduce(lambda x, y : x + y, lista))

print(total)

