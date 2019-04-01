from problema03 import Calc
from numbers import Number

calculadora = Calc()

def exp(x, y, z):
    if isinstance(x, Number) and isinstance(y, Number) and isinstance(z, Number):        
        return calculadora.sub(calculadora.add(x, y), z)
    else:
        raise TypeError("Foram inseridos na função argumentos que não são números.")

if __name__ == "__main__":
    print(exp(3, 3, 2))


