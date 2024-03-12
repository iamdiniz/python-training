'''
escreva um programa que leia a velocidade de um carro. se ele ultrapassar
80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
'''

velocidadeDoUsuario = float(input('Você chegou a quantos Km/h? '))
if velocidadeDoUsuario > 80:
    multa = (velocidadeDoUsuario - 80) * 7
    print('Você foi multado por ultrapassar o limite de 80Km/h, valor a pagar R${:.2f}'.format(multa))
else:
    print('Parabéns, você dirige com moderação! tenha um bom dia')
