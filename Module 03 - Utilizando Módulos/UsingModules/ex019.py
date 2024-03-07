from random import choice

'''
um professor quer sortear um dos seus quatros alunos para apagar o quadro.
faça um programa que ajude ele, lendo o nome deles e escrevendo
o nome do escolhido (sem for)
'''

aluno1 = str(input('Nome do primeiro aluno? '))
aluno2 = str(input('Nome do segundo aluno? '))
aluno3 = str(input('Nome do terceiro aluno? '))
aluno4 = str(input('Nome do quarto aluno? '))

lista = [aluno1, aluno2, aluno3, aluno4]
alunoEscolhido = choice(lista)

print('O aluno escolhido foi {}'.format(alunoEscolhido))