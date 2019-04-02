from collections import Counter


def contador(wordOrList : "List or String") -> Counter:
    """  
    Retorna um collections.Counter com a ocorrência das letras de uma palavra.
    Caso seja inserida uma lista, retorna a ocorrência de um elemento na lista.
    
    Arguments:
        palavra {[list] or [str]} -- [Uma palavra ou lista a ser contada]

    Returns:
        [Counter] -- [um Counter com a frequência dos itens]
    """


    return Counter(wordOrList)
