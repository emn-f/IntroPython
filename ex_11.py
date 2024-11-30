# Nome, idade e nota do aluno
x = 1

dic = {
    "nome": input('Informe o nome do aluno: '),
    "idade": input('Informe a idade do aluno: '),
    "nota": input('Informe a nota do aluno: ')
    }

while (x != 0):
    op = int(input('Qual dado você deseja consultar? 1 - Nome, 2 - Idade, 3 - Nota, 4 - Sair'))
    if (op == 1):
        print(dic["nome"])
    elif (op == 2):
        print(dic["idade"])
    elif (op == 3):
        print(dic["nota"])
    elif (op == 4):
        x = 0