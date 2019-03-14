def isMultiploDe3e5(numero):
    if numero % 5 == 0 and numero % 3 == 0:
        return 'romeu e julieta'
    else:
        return numero

print(isMultiploDe3e5(3))
print(isMultiploDe3e5(5))
print(isMultiploDe3e5(15))
