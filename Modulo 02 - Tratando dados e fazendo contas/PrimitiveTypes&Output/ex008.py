"""
escreva um programa que leia um valor em metros
e o exiba convertido em centímetros e milímetros
"""

metros = float(input('Quantos metros? '))
centimetros = metros * 100
milimetros = metros * 1000
print('{:.2f} metros tem {:.2f} centímetros e {:.2f} milímetros'
      .format(metros, centimetros, milimetros))
