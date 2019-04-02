from exercicio_03 import contador
from exercicio_04 import transformador

def one_function_to_rule_them_all(frase):
    # return (contador(transformador(frase)) if len(transformador(frase)) > 1 else dict())
    return contador(transformador(frase))
