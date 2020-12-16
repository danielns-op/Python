from time import sleep

fib = ['Fi', 'bo', 'na', 'cci']

print('> Sequência de ', end='')
sleep(0.5)
for letra in fib:
    print(letra, end='')
    sleep(0.5)

num = int(input('\nInforme um número: '))
cont = 2
termA, termB = 0, 1
soma = 0
print('{} -> {}'.format(termA, termB), end='')
while cont < num:
    termA, termB = termB, termB + termA
    print(' -> {}'.format(termB), end='')
    cont += 1
