"""
faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
com 5% de desconto.
"""

preco = float(input('Qual o preço do produto? '))
desconto = preco * 0.05
produtoComDescontoAplicado = preco - desconto # prefira sempre fazer as coisas separadas
print('O produto com o novo preço de desconto fica R${:.2f} reais'
      .format(produtoComDescontoAplicado))

# mesmo que a variável fique com um nome grande, escolha a legíbilidade!
