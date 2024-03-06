"""
faça um algoritmo que leia o salário de um funcionário
e mostre seu novo salário. com 15% de aumento.
"""

salario = float(input('Digite seu salário: '))
salarioAumentado = salario + salario * 0.15
print('Seu salário com 15% de aumento fica R${} reais'.format(salarioAumentado))
