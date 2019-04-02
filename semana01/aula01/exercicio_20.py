#Baseando-se nos  exercícios passados, monte um dicionário com os seguintes chaves:
#lista, somatório, tamanho, maior valor e menor valor

lista = [1, 2, 3, 4]
meuDicionario = {'lista' : lista,
                'somatória' : sum(lista),
                'tamanho' : len(lista),
                'maior valor' : max(lista),
                'menor valor' : min(lista)}

print(meuDicionario)