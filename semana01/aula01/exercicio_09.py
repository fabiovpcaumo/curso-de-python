#Faça um oprograma que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e continue pedindo
# até que o usuário informe um valor válido.

valor = -1
while (valor < 0 or valor > 10):
    valor = int(input("Digite um valor entre zero e dez: "))
    if (valor < 0 or valor > 10):
        print("Valor inválido!")

print("Obrigado por colaborar! {}".format(valor))