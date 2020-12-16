from datetime import date

anoatual = date.today().year
maior = 0
menor = 0

for c in range(7):
    ano = int(input('Ano de nascimento {}ª pessoa: '.format(c + 1)))
    if (anoatual - ano) >= 18:
        maior += 1
    else:
        menor += 1

print('Temos {} menores de idade e {} pessoas maior de idade.'.format(menor, maior))
