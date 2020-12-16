from datetime import date
anoAtual = date.today().year
ano = int(input('Ano nascimento: '))

if ano > anoAtual:
    print('Data inválida!')
    exit(1)

idade = anoAtual - ano

if idade <= 9:
    print('Mirim')
elif 9 < idade <= 14:
    print('Infantil')
elif 14 < idade <= 19:
    print('Junior')
elif 19 < idade <= 25:
    print('Sênior')
else:
    print('Master')
