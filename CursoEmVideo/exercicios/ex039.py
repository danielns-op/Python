from datetime import date

anoAtual = date.today().year
# mesAtual = date.today().month
# diaAtual = date.today().day

ano = int(input('Ano de nascimento: '))

if (anoAtual - ano) < 18:
    print('Você ainda vai se alistar.')
    print('Restá apenas {} anos.'.format(18 - (anoAtual - int(ano))))
elif (anoAtual - ano) == 18:
    print('Está na hora de se alistar.')
else:
    print('Passou do tempo de se alistar.')
    print('Você está atrasado {} anos.'.format((anoAtual - int(ano) - 18)))
