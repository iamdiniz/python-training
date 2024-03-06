"""
crie um programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos dólares ela pode comprar
considere
US$1.00 = R$3.27
"""

dinheiro = float(input('Quantos reais você tem? '))
converterRealEmDolar = dinheiro / 3.27
print('Você pode comprar U${:.2f} em dólares'.format(converterRealEmDolar))
