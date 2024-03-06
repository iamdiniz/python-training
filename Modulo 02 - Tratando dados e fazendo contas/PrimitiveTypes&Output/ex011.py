"""
faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta, pinta uma área de 2m².
"""

larguraParede = float(input('Qual a largura da sua parede? '))
alturaParede = float(input('Qual a altura da sua parede? '))

area = larguraParede * alturaParede
litrosDeTintaNecessario = area / 2

print('Você tem uma área de {:.2f}m², será necessário {:.2f} litros de tinta'
      .format(area, litrosDeTintaNecessario))
