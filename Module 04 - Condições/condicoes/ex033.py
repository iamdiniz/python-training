'''
faça um programa que leia três números e mostre qual é o maior e
qual é o menor
'''

primeiroNumero = int(input('Digite o primeiro número: '))
segundoNumero = int(input('Digite o segundo número: '))
terceiroNumero = int(input('Digite o terceiro número: '))

menor = primeiroNumero
if segundoNumero < primeiroNumero and segundoNumero < terceiroNumero:
    menor = segundoNumero
if terceiroNumero < primeiroNumero and terceiroNumero < segundoNumero:
    menor = terceiroNumero

maior = primeiroNumero
if segundoNumero > primeiroNumero and segundoNumero > terceiroNumero:
    maior = segundoNumero
if terceiroNumero > primeiroNumero and terceiroNumero > segundoNumero:
    maior = terceiroNumero

print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
