def calculaMedia(lista):
    media = sum(lista)/len(lista)
    return media

print("Média do aluno de notas 3, 5 e 6.5: {}".format(calculaMedia([3, 5, 6.5])))