valores = ('',)
pares = 0

for n in range(1, 5):
    num = int(input(f'Informe o {n}º valor: '))
    valor = (num,)
    valores += valor
    if num % 2 == 0:
        pares += 1

print(f'Valores informados: {valores[1:]}')
print(f'Foram encontrado(s) {valores.count(9) if 9 in valores else 0} número(s) 9.')
print(f'O primeiro valor 3 está na posição {valores.index(3) if 3 in valores else 0}.')
print(f'Foram encontrado(s) {pares} número(s) par(es).')
