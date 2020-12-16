from time import sleep

ptermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

print('Progressão Aritmética - PA')
print('do termo {} e razão {} é:'.format(ptermo, razao))

termos = ptermo
escolha = 10
cont = 0
quant_termo = escolha

while True:
    print('{} '.format(termos), end='')
    termos += razao
    cont += 1
    if cont == escolha:
        escolha = int(input('\nQuantos termos quer mostrar a mais: '))
        quant_termo += escolha
        cont = 0
        if escolha == 0:
            print('\nSaindo... Ao todo foram mostratos {} termos.'.format(quant_termo))
            sleep(2)
            break
