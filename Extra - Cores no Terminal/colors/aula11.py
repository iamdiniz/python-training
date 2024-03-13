print('\033[mOla Mundo\033[m')
print('\033[2;31mHello World!\033[m')

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))

nome = 'Guilherme'
print('Ola! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7m'}

print('Bem vindo {}{}{}!!!'.format(cores['azul'], nome, cores['limpa']))
print('Prazer em conhecer {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))