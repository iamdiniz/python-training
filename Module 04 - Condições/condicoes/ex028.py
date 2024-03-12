from random import randint
from time import sleep

'''
escreva um programa que faça o computador 'pensar' em un número
inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o
número escolhido pelo computador.
o programa deverá escrever na tela se o usuário venceu ou perde.
'''

print('-=-' * 20)
print('Eai, vai encarar?')
print('-=-' * 20)
numeroDigitado = int(input('Chute entre 0 e 5, qual número eu pensei? '))
numeroQueOComputadorPensou = randint(0, 5)
print('PENSANDO...')
sleep(2)

if numeroDigitado == numeroQueOComputadorPensou:
    print('Parabéns, você acertou o número que eu pensei, que foi {}'.format(numeroQueOComputadorPensou))
else:
    print('Eita, você errou, eu pensei no número {}'.format(numeroQueOComputadorPensou))
