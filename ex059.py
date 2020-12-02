from time import sleep
while True:
    num1 = int(input('Informe o 1º valor: '))
    num2 = int(input('Informe o 2º valor: '))
    escolha = str(input('''Escolha a operação
    [ 1 ] - Somar
    [ 2 ] - Multiplicar
    [ 3 ] - Maior
    [ 4 ] - Novos números
    [ 5 ] - Sair do programa
    Qual opção: '''))
    if escolha == '1':
        print('{} + {} = {}'.format(num1, num2, (num1 + num2)))
    elif escolha == '2':
        print('{} X {} = {}'.format(num1, num2, (num1 * num2)))
    elif escolha == '3':
        if num1 > num2:
            print('O número {} é maior que {}.'.format(num1, num2))
        elif num2 > num1:
            print('O número {} é maior que {}.'.format(num2, num1))
        else:
            print('Os números {} e {} são iguais.'.format(num1, num2))
    elif escolha == '4':
        continue
    elif escolha == '5':
        break
    else:
        print('Opção invalida, tente novamente.')
        sleep(2)
