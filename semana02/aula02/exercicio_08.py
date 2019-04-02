

def sabores_de_pizza():
    ...


def filter_pizzas(valor : float, pizzas : list):
    filtered_pizzas = []
    for pizza in pizzas:
        if pizza != ():
            if pizza[1] < valor:
                filtered_pizzas.append(pizza)
    return filtered_pizzas