'''
refaça o ex35 acrescentando o recurso de mostrar que tipo
de triângulo será formado:
equilátero: todos os lados iguais
isósceles: dois lados iguais
escaleno: todos os lados diferentes
'''

print('Vamos analisar seu triãngulo e dizer qual o tipo dele')
primeiraReta = float(input('Digite o primeiro segmento: '))
segundaReta = float(input('Digite o segundo segmento: '))
terceiraReta = float(input('Digite o terceiro segmento: '))

if (primeiraReta < segundaReta + terceiraReta and segundaReta < primeiraReta
        + terceiraReta and terceiraReta < primeiraReta + segundaReta):
    print('Os segmentos acima PODEM FORMAR UM TRIÂNGULO!')
    if primeiraReta == segundaReta and primeiraReta == terceiraReta:
        print('Esse é um triângulo EQUILÁTERO!')
    elif primeiraReta == segundaReta or segundaReta == terceiraReta or primeiraReta == terceiraReta:
        print('Esse é um triângulo ISÓSCELES!')
    elif primeiraReta != segundaReta and primeiraReta != terceiraReta and terceiraReta != primeiraReta:
        print('Esse é um triângulo ESCALENO!')
else:
    print('Os segmentos acima \033[31mNÃO\033[m PODEM FORMAR UM TRIÂNGULO')
