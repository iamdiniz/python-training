from datetime import date

'''
faça um programa que leia o ano de nascimento
de um jovem e informe, de acordo com sua idade:
se ele ainda vai se alistar ao serviço militar
se é a hora de se alistar
se já passou do tempo do alistamento
seu programa também deverá mostrar o tempo que falta ou que passou do prazo
'''

anoAtual = date.today().year
anoDeNascimento = int(input('Qual seu ano de nascimento? '))
idade = anoAtual - anoDeNascimento
idadeDeAlistamento = 18

print('Se você nasceu em {}, hoje no ano de {} você tem {} anos'
      .format(anoDeNascimento, anoAtual, idade))

if idade == idadeDeAlistamento:
    print('Está no tempo de você se alistar imediatamente!')
elif idade < idadeDeAlistamento:
    quantoTempoFalta = idadeDeAlistamento - idade
    print('Ainda não chegou seu tempo de alistamento')
    print('Faltam {} ano para você se alistar!'.format(quantoTempoFalta))
    anoQueDeveSeAlistar = anoAtual + quantoTempoFalta
    print('Você deve se alistar no ano de {}'.format(anoQueDeveSeAlistar))
elif idade > idadeDeAlistamento:
    tempoQuePassou = idade - idadeDeAlistamento
    print('Já passou do tempo do seu alistamento!')
    print('Se passaram exatamente {} anos des de que você se alistou'.format(tempoQuePassou))
    anoQueDeveriaTerAlistado = anoAtual - tempoQuePassou
    print('Você deveria ter se alistado no ano de {}'.format(anoQueDeveriaTerAlistado))
