"""
escreva um programa que pergunte a quantidade de km percorridos
por um carro alugado e quantidade de dias pelos quais ele foi alugado.
calcule o preço a pagar, sabendo que o carro custa R$60 por dia e
R$0.15 por km rodado
"""

diasAlugado = int(input('Quantos dias você alugou o carro? '))
kmRodado = int(input('Quantos Km rodados? '))

aluguelPorDia = diasAlugado * 60
aluguelKmRodados = kmRodado * 0.15
totalAPagar = aluguelPorDia + aluguelKmRodados

print('O total a pagar é de R${:.2f}'.format(totalAPagar))
