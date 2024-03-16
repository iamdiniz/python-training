"""
elabora um programa que calcule o valor a ser pago por um produto,
considerndo o seu preço normal e condição do pagamento
à vista dinheiro/ cheque: 10% de desconto
à vista no cartão: 5% de desconto
em até 2x no cartão: preço normal
3x ou mais no cartão: 20% de juros
"""

print('-=-' * 20)
print('Olá, bem vindo')
produto = float(input('Qual o preço do produto R$'))
formaDePagamento = float(
    input('''Qual a forma de pagamento?
[1] - à vista no dinheiro
[2] - à vista no cartão
[3] - parcelar 2x no cartão
[4] - parcelar 3x ou mais no cartão
Qual opção: '''))

if formaDePagamento == 1:
    desconto = produto * 0.1
    produtoComDescontoAplicado = produto - desconto
    print('O produto à vista fica por R${:.2f} reais com 10% de desconto!!'.format(produtoComDescontoAplicado))

elif formaDePagamento == 2:
    descontoNoCartao = produto * 0.05
    produtoComDescontoAplicado = produto - descontoNoCartao
    print('O produto à vista no cartão fica por R${:.2f} reais com 5% de desconto!!!'
          .format(produtoComDescontoAplicado))

elif formaDePagamento == 3:
    produtoParceladoDuasX = produto / 2
    print('Sua compra será parcelada em 2x ficando por R${:.2f}'.format(produtoParceladoDuasX))
    print('O produto fica por R${:.2f} reais em 2x no cartão, sem juros, preço normal'.format(produto))

elif formaDePagamento == 4:
    quantidadeParcelas = int(input('Quantas parcelas: '))
    juros = produto * 0.2
    produtoComJuros = produto + juros
    produtoParcelado = produtoComJuros / quantidadeParcelas
    print('Sua compra será parcelada em {}x ficando por R${:.2f}'.format(quantidadeParcelas, produtoParcelado))
    print('O produto fica com 20% de juros ficando por R${:.2f} reais no preço final'
          .format(produtoComJuros))
else:
    print('Você digitou um número fora das opções sugeridas, tente novamente dentro das opções 1, 2, 3 e 4')
