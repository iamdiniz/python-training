'''
desenvolva um programa que pergunte a distância de uma viagem em Km.
calcule o preço da passagem, cobrando R$0,50 por Km para viagens
de até 200Km e R$0,45 para viagens mais longas.
'''

distanciaViagem = float(input('Qual é a distância da viagem? '))
print('Uma viagem de {}Km.'.format(distanciaViagem))
if distanciaViagem > 200:
    precoPassagem = distanciaViagem * 0.45
else:
    precoPassagem = distanciaViagem * 0.50
print('O preço a ser pago pela viagem é de R${:.2f} reais'.format(precoPassagem))
