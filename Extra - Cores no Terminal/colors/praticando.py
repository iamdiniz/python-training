from random import randint
from time import sleep

cores = {'limpar': '\033[m',
         'red': '\033[31m',
         'purple': '\033[35m',
         'redUnderlined': '\033[4;31m',
         'yellow': '\033[33m',
         'yellowUndelined': '\033[1;33m',
         'blueUnderlined': '\033[1;34m',
         'blue': '\033[34m'}

print('{}-=-'.format(cores['red']) * 20)
print('{}ADIVINHE{} O {}NÚMERO{} QUE EU {}PENSEI{}!! HA HA HA HA HA !!!!! (¬_¬)'.
      format(cores['yellowUndelined'],
             cores['purple'],
             cores['yellowUndelined'],
             cores['purple'], cores['blueUnderlined'],
             cores['red']))
print('LUTE COMIGO! OU MORRA TENTANDO!!')
print('{}-=-'.format(cores['red']) * 20)

numeroDigitado = int(input('{}DIGITE UM NÚMERO ENTRE 0 A 5 QUE O COMPUTADOR PENSOU: {}'.
                           format(cores['blue'], cores['limpar'])))
numeroQueOComputadorPensou = randint(0, 5)

print('{}LUTANDO!!...'.format(cores['red']))
sleep(2)

if numeroDigitado == numeroQueOComputadorPensou:
    print('{}CONGRATULATIONS!!!'.format(cores['blue']))
    print('{}COMPUTADOR: O QUE? IMPOSSIVEL, NÃAAAAAAAAOOOOOOOOO, VOCÊ ME VENCEU!'.format
          (cores['red']))
    print('{}YOU WON!!, O NÚMERO QUE O COMPUTADOR PENSOU FOI {}'.format(cores['blue'], numeroQueOComputadorPensou))
else:
    print('MORRRAAAAAAAAAAA, VÁ PARA OUTRA DIMENSÃO!!')
    print('YOU LOSE, o número que o computador pensou foi {}'.format(numeroQueOComputadorPensou))
