p = float(input('Preço do produto: R$'))
np = p - (p * 0.05)

print('Preço: R$ {:.2f}\nDesconto: 5%\nNovo preço: R$ {:.2f}'.format(p, np))
