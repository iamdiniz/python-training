from datetime import date

'''
faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
ano bissexto precisa ser divissivel por 4
exceto aqueles que são multiplos de 100 que não são multiplos de 400
'''

ano = int(input('Digite um ano qualquer: (Coloque 0 para analisar o ano atual:) '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))