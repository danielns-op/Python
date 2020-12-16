cidade = str(input('Informe o nome da cidade: ')).strip()
c = cidade.split()
print('Começa com SANTO: {}'.format('SANTO' in c[0].upper()))
