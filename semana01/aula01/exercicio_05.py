#Faça um programa para a leitura de duas notas parciais de um aluno.
#O programa deve calcular a média alcançada por aluno e apresentar:
#- A mensagem "Aproado", se a média for alcançada for maior ou igual a sete
#- A mensagem "Reprovado", se a media for menor do que sete
#- A mensagem "Aprovado com Distinção", se a média for igual a dez

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
status = ""

if media >= 10:
    status = "Aprovado com Distinção"
elif media >= 7:
    status = "Aprovado"
else:
    status = "Reprovado"

print("A média do aluno foi: {}. \nO status do aluno é: {}".format(media, status))

