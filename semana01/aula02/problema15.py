def soma_2(n):
    return n + 2

def subtrai_2(n):
    return n - 2

def twice(f, val):
    return f(f(val))

print(twice(soma_2, 2))