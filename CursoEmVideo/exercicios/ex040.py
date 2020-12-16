na = float(input('Nota 1: '))
nb = float(input('Nota 2: '))

media = (na + nb) / 2

if media < 5.0:
    print('REPROVADO.')
elif 5.0 < media < 6.9:
    print('RECUPERAÇÃO.')
else:
    print('APROVADO!!!')
