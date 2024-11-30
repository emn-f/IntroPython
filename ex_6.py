# Exibir maior número
num1 = int(input('Infomre o 1º número: '))
num2 = int(input('Infomre o 2º número: '))
num3 = int(input('Infomre o 3º número: '))

maior = num1

if (num2 > maior):
    maior = num2
if (num3 > maior):
    maior = num3

print('Maior número: ', maior)