'''
desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo
'''

print('Vamos analisar esse triângulo? Diga as retas')
primeiraReta = float(input('Primeiro segmento: '))
segundaReta = float(input('Segundo segmento: '))
terceiraReta = float(input('Terceiro segmento: '))
if (primeiraReta < segundaReta + terceiraReta and segundaReta
        < primeiraReta + terceiraReta and terceiraReta < primeiraReta + segundaReta):
    print('Os segmentos mencionados PODEM formar um triângulo!')
else:
    print('Os segmentos mencionados NÃO podem formar um triãngulo')
