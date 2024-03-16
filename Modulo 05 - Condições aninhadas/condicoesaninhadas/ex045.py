from random import randint
from time import sleep
from sys import exit

"""
crie um programa que faça o computador jogar
Jokenpô com você
"""

print('-=' * 20)
print('Lets play baby')
jogadasPossiveis = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''JOKENPÔ
0 - Pedra
1 - Papel
2 - Tesoura''')
print('-=' * 20)

jogador = int(input('O que deseja jogar: '))
if jogador > 2 or jogador < 0:
    print('JOGADA INVÁLIDA, tente novamente digitando um número de 0 a 2 que são as jogadas possíveis!')
    exit()

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')
print('O computador jogou {}'.format(jogadasPossiveis[computador]))
print('Você jogou {}'.format(jogadasPossiveis[jogador]))

if computador == 0:
    if jogador == 0:
        print('EMPATOU!')
    if jogador == 1:
        print('VOCÊ VENCEU!')
    if jogador == 2:
        print('COMPUTADOR VENCEU')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    if jogador == 1:
        print('EMPATOU')
    if jogador == 2:
        print('VOCÊ VENCEU!')
elif computador == 2:
    if jogador == 0:
        print('VOCÊ VENCEU!')
    if jogador == 1:
        print('COMPUTADOR VENCEU!')
    if jogador == 2:
        print('EMPATE!')
else:
    print('Jogada inválida, tente novamente digitando um número de 0 a 2 que são as jogadas possíveis!')
