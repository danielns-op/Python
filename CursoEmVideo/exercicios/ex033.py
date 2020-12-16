a = int(input('Informe o número 1: '))
b = int(input('Informe o número 2: '))
c = int(input('Informe o número 3: '))

if b < a > c:
    maior = a
if a < b > c:
    maior = b
if a < c > b:
    maior = c
if b > a < c:
    menor = a
if a > b < c:
    menor = b
if a > c < b:
    menor = c

print('O número {} é o maior.'.format(maior))
print('O número {} é o menor.'.format(menor))
