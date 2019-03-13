state = 10

def soma_2(n):
    return n + 2

def sub_2(n):
    return n - 2

def compose(*funcs):
    def inner(arg):
        state = arg
        for f in reversed(funcs):
            print(f, state)
            state = f(state)
        return state
    return inner

#L = [soma_2, sub_2]
#L[0](2)
#print(L)
print(compose(soma_2, sub_2))