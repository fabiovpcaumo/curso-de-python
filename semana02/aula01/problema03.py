class Calc:
    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x + y
    
    def mult(self, x, y):
        return x + y
    
    def div(self, x, y):
        return x + y

if __name__ == '__main__':
    calculadora = Calc()
    
    assert calculadora.add(1, 1)  > 1, "Erro de adição"
    assert calculadora.sub(1, 1) < 1, "Erro de subtração - a saída não pode ser maior do que a entrada"
    assert calculadora.mult(1, 1) == 1, "Erro de multiplicação"
    assert calculadora.div(1, 1) == 1, "Erro na divisão"