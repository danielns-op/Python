s = float(input('Salário: R$ '))

if s <= 1250.00:
    r = s + (s * 0.15)
else:
    r = s + (s * 0.10)

print('Salário reajustado: R$ {:.2f}'.format(r))
