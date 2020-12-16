cont = 1
soma = 0
maior = 0
menor = 0
while True:
    num = int(input('Informe um número: '))
    soma += num
    if cont == 1:
        maior = num
        menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    escolha = str(input('Deseja continuar a digitar [S/N]: ').upper().strip())
    if escolha == 'S':
        cont += 1
        continue
    else:
        break

print('\nVocê digitou {} números.'.format(cont))
print('A média de todos os números digitados é: {}'.format(soma / cont))
print('O maior número é {} e o menor número é {}.'.format(maior, menor))
