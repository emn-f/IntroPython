alunos = []


def menu():
    print('MENU')
    print('1 - Cadastrar aluno \n'
          '2 - Listar alunos \n'
          '3 - Analisar notas \n'
          '4 - Modificar nota \n'
          '5 - Remover aluno \n'
          '6 - SAIR')


def cadastrar_aluno():
    nome = input('Informe o nome do aluno: ')
    idade = int(input('Informe a idade: '))
    nota = float(input('Informe a nota: '))
    alunos.append({'nome': nome, 'idade': idade, 'nota': nota})


def listar_alunos():
    for aluno in alunos:
        print(f'Nome: {aluno['nome']}, Idade: {aluno['idade']}. Nota: {aluno['nota']}')
    print(f'Quantidade de alunos: {len(alunos)}')


def analisar_notas():
    if not alunos:
        print('Sem alunos cadastrados :/')
        return
    media = sum(aluno['nota'] for aluno in alunos)
    aprovados = [aluno for aluno in alunos if aluno['nota'] >= 7]

    print(f'A média das notas é: {media:.2f}')
    print('Aluno aprovado.')
    for aluno in aprovados:
        print(f'Aluno: {aluno['nome']}. Nota {aluno['nota']}')


def alterar_nota():
    nome = input('Informe o nome do aluno: ')
    for aluno in alunos:
        if nome == aluno['nome']:
            aluno['nota'] = float(input('Informe a nova nota: '))
            print('Nota modificada.')
            return
    print('Aluno não encontrado.')


def remover_aluno():
    nome = input('Digite o nome do aluno que deseja remover: ')
    for aluno in alunos:
        if nome == aluno[nome]:
            alunos.remove(aluno)
            print('Aluno removido.')
            return
    print('Aluno não encontrado.')


check = True

while check:
    menu()
    op = int(input('Escolha uma opção: '))
    match op:
        case 1:
            cadastrar_aluno()
        case 2:
            listar_alunos()
        case 3:
            analisar_notas()
        case 4:
            alterar_nota()
        case 5:
            remover_aluno()
        case 6:
            check = False
