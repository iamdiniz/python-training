'''
escreva um programa que pergunte o salário de
um funcionário e calcule o valor do seu aumento.
para salários superiores a 1.250.00. calcule um aumento
de 10%
para os inferiores ou iguais, o aumento é de 15%
'''

salario = float(input('Digite seu salário: '))
if salario > 1250:
    aumentoDoSalario = salario + salario * 0.10
    print('Seu salário de R${:.2f} aumentou em 10% e passa a ser R${:.2f}'.format(salario, aumentoDoSalario))
else:
    aumentoDoSalario = salario + salario * 0.15
    print('Seu salário de R${:.2f} aumentou em 15% e passa a ser R${:.2f}'.format(salario, aumentoDoSalario))