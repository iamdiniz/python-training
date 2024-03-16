"""
escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa. O programa vai perguntar o valor
da casa, o salário do comprador e em quantos anos
ele vai pagar.
Calcule o valor da prestação mensal. sabendo que ela não pode exceder 30%
do salário ou então o empréstimo será negado
"""

print('Tudo bem? seja bem vindo, você quer fazer um emprèstimo?')
valorDaCasa = float(input('Qual é o valor da casa: R$'))
salarioDoUsuario = float(input('Qual seu salário amigo: R$'))
quantosAnosVaiPagar = int(input('Quantos anos de financiamento? '))

anosEmMeses = quantosAnosVaiPagar * 12
prestacaoMensal = valorDaCasa / anosEmMeses
limiteMinimo = salarioDoUsuario * 0.3

print('Para efetuar o pagamento de R${:.2f} em {} anos'.format(valorDaCasa, quantosAnosVaiPagar), end='')
print(' a prestação será de R${:.2f}'.format(prestacaoMensal))

if prestacaoMensal <= limiteMinimo:
    print('Empréstimo CONCEDIDO!')
else:
    print('Empréstimo NEGADO')