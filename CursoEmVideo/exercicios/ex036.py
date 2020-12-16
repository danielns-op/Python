vc = float(input("Valor da casa: R$ "))
sl = float(input("Salário: R$ "))
ap = int(input("Quantidade de anos para pagar: "))

qp = ap * 12
pm = vc / qp

print('\nValor da casa: R$ {:.2f}'.format(vc))
print('Quantidade de parcelas: {}'.format(qp))
print('Seu salário: R$ {:.2f}'.format(sl))
print('Valor das prestações: R$ {:.2f}\n'.format(pm))

if pm < (sl * 0.3):
    print('Empréstimo aprovado!')
else:
    print('Emprestimo negado.')
    print('Valor das prestações exedeu 30% do seu salário.')
    print('30% do seu salário: R$ {:.2f}'.format(sl * 0.3))
