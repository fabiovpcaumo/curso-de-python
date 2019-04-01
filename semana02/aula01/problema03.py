class Calc:
    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y
    
    def mult(self, x, y):
        return x * y
    
    def div(self, x, y):
        return x / y

if __name__ == '__main__':
    print("oi mundo")
    calculadora = Calc()
    
    #SUTs
    # assert calculadora.add(1, 1)  > 1, "Erro de adição"
    # assert calculadora.sub(1, 1) < 1, "Erro de subtração - a saída não pode ser maior do que a entrada"
    # assert calculadora.mult(1, 1) == 1, "Erro de multiplicação"
    # assert calculadora.div(1, 1) == 1, "Erro na divisão"

    #Agora que você tem os testes para garantir o comportamaento dos seus métodos. Você poderia efeuar a correção da classe sem grandes problemas?
    #R.: Sim, pois os testes unitários possuem um grande code coverage, garantindo que terei feedback sobre as alterações realizadas

    #Dada que exista uma função de soma e uma de subtração.
    #f(x, y, z) -> x + y - z
