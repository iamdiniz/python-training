'''
desenvolva uma lógica que leia o peso e a altura de uma
pessoa, calcule seu IMC e mostre seu status, de acordo com a
tabela abaixo:
Abaixo de 18.5: abaixo do peso
Entre 18.5 e 25: peso ideal
25 até 30: Sobrepeso
30 até 40: Obesidade
acima de 40: Obesidade mórbida
'''

print('Vamos saber seu IMC?')
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

imc = peso / (altura * altura)

if imc < 18.5:
    print('Você está abaixo do PESO NORMAL!, seu IMC é igual à {:.1f}'.format(imc))
elif imc < 25:
    print('Você está no peso ideal, seu IMC é igual à {:.1f}'.format(imc))
elif imc < 30:
    print('SOBREPESO!, seu IMC é igual à {:.1f}'.format(imc))
elif imc < 40:
    print('OBESIDADE!, seu IMC é igual à {:.1f}'.format(imc))
elif imc > 40:
    print('OBESIDADE MÓRBIDA! TOME CUIDADO, seu IMC é igual à {:.1f}'.format(imc))
