from problema03 import Calc

calculadora = Calc()

def exp(x, y, z):
    return calculadora.sub(calculadora.add(x, y), z)

def expexp(x, y, z):
    return exp(exp(x, y, z), y, z)

if __name__ == "__main__":
    print(exp(3, 3, 2))
    print(expexp(3, 2, 1))


