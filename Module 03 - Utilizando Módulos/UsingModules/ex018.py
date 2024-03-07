from math import radians, sin, cos, tan

'''
faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
cossano e tangente desse ângulo.
'''

angulo = float(input('Digite um ângulo qualquer: '))
anguloEmRadiano = radians(angulo)

seno = sin(anguloEmRadiano)
cosseno = cos(anguloEmRadiano)
tangente = tan(anguloEmRadiano)

print('O seno de {} é {:.2f}'.format(angulo, seno))
print('O cosseno de {} é {:.2f}'.format(angulo, cosseno))
print('A tangente de {} é {:.2f}'.format(angulo, tangente))
