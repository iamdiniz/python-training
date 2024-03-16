'''
crie um programa que leia duas notas de um aluno e calcule sua média
mostrando uma mensagem no final, de acordo com a média
atingida
media abaixo de 5.0 reprovado
media entre 5.0 e 6.9 recuperação
media 7.0 ou superior aprovado
'''

primeiraNota = float(input('Qual foi sua primeira nota? '))
segundaNota = float(input('Qual foi sua segunda nota? '))
media = (primeiraNota + segundaNota) / 2

if media < 5.0:
    print('Sua média foi {:.1f} \n Você foi REPROVADO! Estude mais'.format(media))
elif media >= 5.0 and media <= 6.9:
    print('Sua média foi {:.1f} \n Estude, você está em RECUPERAÇÃO'.format(media))
else:
    print('Sua média foi {:.1f} \n Parabéns, você foi APROVADO!'.format(media))