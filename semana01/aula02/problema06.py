lista = list(range(1, 31))
resultado = ["pin" if x%4==0 else x for x in lista]

print(resultado)