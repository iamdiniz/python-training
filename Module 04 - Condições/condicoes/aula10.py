# nome = str(input('Qual é o seu nome? '))
# if nome == 'Guilherme':
#     print('Que nome lindo')
# else:
#     print('Seu nome é tão normal')
# print('Bom dia, {}'.format(nome))

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('A sua média foi {:.1f}'.format(media))

print('Parabèns' if media >= 6.0 else 'Estude mais!')

# if media >= 6.0:
#     print('Sua média foi boa! Congratulations')
# else:
#     print('Sua média foi ruim! Estude mais')
