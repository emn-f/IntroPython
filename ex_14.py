# Função pra receber uma lista de números e retornar a soma deles
lista = []

x = int(input('Informe o tamanho da lista: '))

for i in range(0, x):
    lista.append(int(input(f'Informe um número: Posição {i + 1}: ')))


def notas_lista(lista):
    return sum(lista)

print('Soma = ', notas_lista(lista))
