from math import trunc

'''
crie um programa que leia um número real qualquer pelo teclado
e mostre na tela a sua porção inteira.
'''

numero = float(input('Digite um número real: '))
print('A parte inteira desse número é {}'.format(trunc(numero)))
