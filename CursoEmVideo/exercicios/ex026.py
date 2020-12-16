f = str(input('Frase: ')).strip()

print('Quantas vezes aparece a letra "A": {}'.format(f.upper().count('A')))
print('Em que posição ela aparece a primeira vez: {}'.format(f.upper().find('A') + 1))
print('Em que posição ela aparece a última vez: {}'.format(f.upper().rfind('A') + 1))
