"""
escreva um programa que converta uma temperatura digitada
em Celsius e converta para Fahrenheit
"""

celsius = int(input('Quantos graus Celsius? '))
fahrenheit = ((9 * celsius) / 5) + 32
print('A temperatura em Fahrenheit é de {}F'.format(fahrenheit))
