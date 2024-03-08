frase = 'Guilherme Kauã Diniz Cabral'

print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])

print(frase.upper().count('A'))
print(len(frase))
print(len(frase.strip()))
print(frase.replace('Kauã', 'Apostolo'))
print(frase)

frase = frase.replace('Kauã', 'Kratos')
print(frase)

print('Guilherme' in frase)
print(frase.find('Guilherme'))
print(frase.find('Danosse'))

print(frase.lower().find('guilherme'))

print(frase.split())
dividido = frase.split()
print(dividido)
print(dividido[0])
print(dividido[0][2])