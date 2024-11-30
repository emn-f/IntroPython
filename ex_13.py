# Função que pra receber e exibir nome e len

nome = input('Informe seu nome: ')

def welcome(nome):
    return f'Olá {nome}!. {nome} possui {len(nome)} dígitos.'

welcome(nome)