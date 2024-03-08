'''
faça um programa que leia o nome completo de uma pessoa
mostrando em seguida o primeiro e o último nome
separadamente
Ana Maria de Souza
Ana
Souza
'''

nome = str(input('Digite seu nome: '))
nomeDividido = nome.split()
print('Seu primeiro nome separado é {}'.format(nomeDividido[0]))
print('Seu ultimo nome separado é {}'.format(nomeDividido[-1]))
