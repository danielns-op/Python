n = int(input('Número: '))
bc = str(input('''Qual a base de conversão:
                  1 - Binário
                  2 - Octal
                  3 - Hexadecimal\nOpção: '''))
valor = n
num = ''

if bc == '1':
    while n // 2 != 0:
        mod = (n % 2)
        num = num + str(mod)
        n = n // 2
    mod = (n % 2)
    num = num + str(mod)
    print('O número {} equivale a {} em binário.'.format(valor, num[::-1]))
elif bc == '2':
    while n // 8 != 0:
        mod = (n % 8)
        num = num + str(mod)
        n = n // 8
    mod = (n % 8)
    num = num + str(mod)
    print('O número {} equivale a {} em octal.'.format(valor, num[::-1]))
elif bc == '3':
    while n // 16 != 0:
        mod = (n % 16)
        if mod in [10, 11, 12, 13, 14, 15]:
            if mod == 10:
                mod = 'A'
            if mod == 11:
                mod = 'B'
            if mod == 12:
                mod = 'C'
            if mod == 13:
                mod = 'D'
            if mod == 14:
                mod = 'E'
            if mod == 15:
                mod = 'F'
        num = num + str(mod)
        n = n // 16
    mod = (n % 16)
    if mod in [10, 11, 12, 13, 14, 15]:
        if mod == 10:
            mod = 'A'
        if mod == 11:
            mod = 'B'
        if mod == 12:
            mod = 'C'
        if mod == 13:
            mod = 'D'
        if mod == 14:
            mod = 'E'
        if mod == 15:
            mod = 'F'
    num = num + str(mod)
    print('O número {} equivale a {} em hexadecimal.'.format(valor, num[::-1]))
else:
    print('Opção "{}" inválida.'.format(n))

'''
Resolução do Gustavo Guanabara:

num = int(input('Digite um número inteiro: '))
print("""Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL""")
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida, tente novamente')
'''