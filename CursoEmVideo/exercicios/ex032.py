from datetime import date
a = int(input('Informe um ano: '))

if a % 4 == 0:
    if a % 100 == 0:
        if a % 400 == 0:
            print('O ano {} é bissexto.'.format(a))
        else:
            print('O ano {} não é bissexto.'.format(a))
    else:
        print('O ano {} é bissexto.'.format(a))
else:
    print('O ano {} não é bissexto.'.format(a))


# Resolução do Gustavo Guanabara
ano = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('O ano {} é BISSEXTO!'.format(a))
else:
    print('O ano {} não é bissexto.'.format(a))

print('Esse ano é {}.'.format(ano))
