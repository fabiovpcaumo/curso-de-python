import re

dataNascimento = ""

"""
while True:
    dataNascimento = input("Insira sua data de nascimento no formato dd/mm/yyyy: ")
    if not re.match("[0-9]{2}\/[0-9]{2}\/[0-9]{4}", dataNascimento):
        print("A data de nascimento está num formato inválido.")
    else:
        break
"""
dataNascimento = input("Insira sua data de nascimento no formato dd/mm/yyyy: ")
dataTratada = dataNascimento.split('/')
print("Você nasceu em {} de {} de {}".format(dataTratada[0], dataTratada[1], dataTratada[2]))
