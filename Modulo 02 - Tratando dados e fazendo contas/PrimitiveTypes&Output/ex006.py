# crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raizQuadrada = numero ** (1 / 2)
print('O dobro de {} é {}, o triplo dele é {}, e sua raiz quadrada é {:.3f}'
      .format(numero, dobro, triplo, raizQuadrada))
