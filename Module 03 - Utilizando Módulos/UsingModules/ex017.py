from math import hypot

'''
faça um programa que leia o comprimento do cateto oposto e do
cateto adjacente de um triângulo retângulo, calcule e mostre
o comprimento da hipotenusa.
'''

catetoOposto = float(input('Comprimento do cateto oposto: '))
catetoAdjacente = float(input('Comprimento do cateto adjacente: '))

# somaEPotenciaCatetos = (pow(catetoOposto, 2)) + (pow(catetoAdjacente, 2))
# raizHipotenusa = sqrt(somaEPotenciaCatetos)
hipotenusa = hypot(catetoOposto, catetoAdjacente)

print('O comprimento da hipotenusa é {:.2f}'.format(hipotenusa))
