from datetime import date

'''
a confederação nacional de natação precisa de um programa
que leia o ano de nascimento de um atleta e mostre sua categoria,
de acordo com a idade
até 9 anos: MIRIM
até 14 anos: INFANTIL
até 19 anos: JUNIOR
até 20 anos: SÊNIOR
Acima: MASTER
'''

anoAtual = date.today().year
print('Olá nadador! Vamos classificar sua categoria')
anoNascimento = int(input('Digite seu ano de nascimento: '))
idade = anoAtual - anoNascimento
print('Em {} você tem {} anos'.format(anoAtual, idade))

if idade <= 9:
    print('Sua catégoria é MIRIM')
elif idade <= 14:
    print('Sua catégoria é INFANTIL')
elif idade <= 19:
    print('Sua catégoria é JUNIOR')
elif idade <= 25:
    print('Sua catégoria é SÊNIOR')
else:
    print('Sua catégoria é MASTER')