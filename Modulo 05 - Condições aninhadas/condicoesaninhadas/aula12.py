nome = str(input('Qual é seu nome: '))
if nome == 'Gui':
    print('Que nome bonito!')
elif nome == 'Diniz' or nome == 'Cabral':
    print('Que nome diferenciado!')
elif nome in 'Ana Cláudia Jéssica Juliana Amanda':
    print('Belo nome feminino')

print('Seu nome é bem normal')
print('Tenha um bom dia, {}!'.format(nome))
