from random import shuffle

'''
o mesmo professor do desafio anterior quer sortear a ordem de apresentação
de trabalhos dos alunos. faça um programa que leia o nome dos quatro
alunos e mostre a ordem sorteada.
'''

grupo1 = str(input('Primeiro grupo: '))
grupo2 = str(input('Segundo grupo: '))
grupo3 = str(input('Terceiro grupo: '))
grupo4 = str(input('Quarto grupo: '))

lista = [grupo1, grupo2, grupo3, grupo4]
shuffle(lista)

print('A ordem de apresentação será: ')
print(lista)
