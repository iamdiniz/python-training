'''
crie um programa que leia o nome de uma pessoa e diga se
ela tem SILVA no nome
'''

nome = str(input('Digite seu nome: ')).strip()
print('Você tem SILVA no nome?', 'SILVA' in nome.upper())
