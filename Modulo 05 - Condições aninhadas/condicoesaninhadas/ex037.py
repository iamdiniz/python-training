'''
escreva um programa que leia um número inteiro
qualquer e peça para o usuário escolher qual será a base
de conversão
1 para binário
2 para octal
3 para hexadecimal
'''

numero = int(input('Digite um número inteiro qualquer: '))
print('''Escolha uma das bases para a coversão:'
      '[1] BIÁRIO'
      '[2] OCTAL'
      '[3] HEXADECIMAL''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} convertido para biário é igual à {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('{} convertido para octal é igual à {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('{} convertido para hexadecimal é igual à {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida. Você digitou um opção que não existe, digite 1, 2 ou 3 nas opções.')
