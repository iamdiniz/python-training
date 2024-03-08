'''
faça um programa que leia uma frase pelo teclado e mostre
quantas vezes aparece a letra 'A'
em que posição ela aparece a primeira vez
em que posição ela aparece a última vez
'''

frase = str(input('Digite uma frase qualquer: '))
print('Nessa frase a letra A aparece {} vez'.format(frase.count('A')))
print('A letra A aparece pela primeira vez na posição {}'.format(frase.find('A')))
print('E a letra A aparece pela última vez na posição {}'.format(frase.rfind('A')))
