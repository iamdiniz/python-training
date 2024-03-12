'''
crie um programa que leia um número inteiro e mostre na
tella se ele é PAR ou IMPAR
'''

numero = int(input('Digite um número: '))
if numero % 2 == 0:
    print('O número {} é PAR'.format(numero))
else:
    print('O número {} é IMPAR'.format(numero))
