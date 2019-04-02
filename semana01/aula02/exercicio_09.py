def cumprimento(saudacao, nome):
    return "{}, {}".format(saudacao, nome)


saudacao = input("Digite uma saudação: ")
nome = input("Digite o nome de quem será saudado: ")
print(cumprimento(saudacao, nome))
