'''
escreva um programa que leia dois números inteiros e
compare-os, mostrando na tela uma mensagem
O primeiro valor é maior
O segundo valor é maior
Não existe valor maior, os dois são iguais
'''

primeiroNumero = int(input('Digite um número inteiro: '))
segundoNumero = int(input('Digite outro número inteiro: '))

if primeiroNumero > segundoNumero:
    print('O PRIMEIRO valor é MAIOR, número {} é o vencedor'.format(primeiroNumero))
elif segundoNumero > primeiroNumero:
    print('O SEGUNNDO valor é MAIOR, número {} é o vencedor'.format(segundoNumero))
else:
    print('Ops, não existe valor maior, os dois são IGUAIS!!')