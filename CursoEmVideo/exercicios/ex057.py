while True:
    sexo = str(input('Qual o Sexo [M/F]: ')).strip().upper()
    if sexo == 'M' or sexo == 'F':
        print('Seu sexo é: {}'.format(sexo))
        break
    else:
        print('Informe apenas M ou F.')
