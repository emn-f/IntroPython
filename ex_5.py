# Classificação de pessoas pro faixa etária

idade = int(input('Informe sua idade: '))

if (idade <= 12):
    print(f'{idade} ano(s). Criança!')
elif (idade <= 17):
    print(f'{idade} anos. Adolescente!')
elif (idade <= 64):
    print(f'{idade} anos. Adulto!')
elif (idade > 64):
    print(f'{idade} anos. Idoso!')