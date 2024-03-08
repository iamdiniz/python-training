'''
crie um programa que leia o nome de uma cidade
e diga se ela começa ou não com o nome "SANTO"
'''

cidade = str(input('Digite um nome de uma cidade: '))
nomeDaCidadeDividido = cidade.split()
print('A cidade tem começa com SANTO?', 'SANTO' in nomeDaCidadeDividido[0])
