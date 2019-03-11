#Problema #03
#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados
#  da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é 
# vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidade de latas
#  de tinta a serem compradas e o preço total.

areaAPintar = int(input('Quantos metros quadrados você precisa pintar?'))
litrosNecessarios = areaAPintar/3

if not(litrosNecessarios.is_integer()):
    litrosNecessarios = (litrosNecessarios//1) + 1

latasNecessarias = litrosNecessarios/18

if not(latasNecessarias.is_integer()):
    latasNecessarias = (latasNecessarias//1) + 1

valorAPagar = latasNecessarias * 80
#DEBUG
print("\nLitros necessários: {}".format(litrosNecessarios))
print("\nLatas necessárias: {}".format(latasNecessarias))
print("\nValor a pagar: R$ {}".format(valorAPagar))