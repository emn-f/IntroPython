# Calcular média de lista de números

fim = False
i = 0
soma = 0
lista = []

print('Digite S para Sair.')

while (not fim):
    lista.append(input(f'Informe um número: Posição {i + 1}: '))
    if (lista[i] == 'S'):
        lista.remove('S')
        fim = True
        print('Programa finalizado.')
        print(f'Tamanho da lista: {len(lista)}')
        print(lista)
        print('Média = ', media)
    else:
        soma += int(lista[i])
        media = soma/len(lista)
        print('Média = ', media)
        i = i + 1
