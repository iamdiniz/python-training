'''
crie um programa que leia o nome de uma cidade
e diga se ela começa ou não com o nome "SANTO"
'''

cidade = str(input('Digite o nome de uma cidade: ')).strip()
print('A cidade começa com Santo?',cidade[:5].upper() == 'SANTO')
