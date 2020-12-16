print('Caixa eletrônico')
print('-=' * 10)
print('{:^20}'.format('Saque Fácil'))
print('=-' * 10)

cedulas_no_caixa = [50, 20, 10, 1]
conta_cinquenta = conta_vinte = conta_dez = conta_um = 0

valor_saque = int(input('Qual valor a ser sacado: '))
contador = total = 0

while total < valor_saque:
    if total + cedulas_no_caixa[contador] > valor_saque:
        contador += 1
    else:
        total += cedulas_no_caixa[contador]
        if cedulas_no_caixa[contador] == 50:
            conta_cinquenta += 1
        if cedulas_no_caixa[contador] == 20:
            conta_vinte += 1
        if cedulas_no_caixa[contador] == 10:
            conta_dez += 1
        if cedulas_no_caixa[contador] == 1:
            conta_um += 1

if conta_cinquenta:
    print(f'[{conta_cinquenta}] notas de R$ 50.00')
if conta_vinte:
    print(f'[{conta_vinte}] notas de R$ 20.00')
if conta_dez:
    print(f'[{conta_dez}] notas de R$ 10.00')
if conta_um:
    print(f'[{conta_um}] notas de R$ 1.00')

print(f'Receba o valor de R$ {total:.2f}')
print('==' * 10)
