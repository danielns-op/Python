ptermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termos = ptermo
print('Progressão Aritmética - PA')
print('do termo {} e razão {} é:'.format(ptermo, razao))
escolha = 10
cont = 0
while True:
    print('{} '.format(termos), end='')
    termos += razao
    cont += 1
    if cont == escolha:
        escolha = int(input('\nQuantos termos quer mostrar a mais: '))
        cont = 0
        if escolha == 0:
            print('\nSaindo...')
            break
