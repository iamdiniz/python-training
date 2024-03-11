'''
crie um programa que leia o nome completo de uma pessoa e mostre
o nome com todas as letras maiúsculas
o nome com todas minúsculas
quantas letras ao tod. sem considerar espaços
quantas letras em o primeiro nome
'''

nome = str(input('Qual o seu nome: ')).strip()

print('Seu nome em maiúsculo fica {}'.format(nome.upper()))
print('Seu nome em minúsculo fica {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome.replace(" ", ""))))

primeiroNome = nome.split()

print('Seu primeiro nome tem {} letras'.format(len(primeiroNome[0])))
