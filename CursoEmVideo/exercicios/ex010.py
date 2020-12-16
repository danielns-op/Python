real = float(input('Quantidade de dinheiro na carteira: R$ '))
dolarComprar = real / 5.70
euroComprar = real / 6.68
libraComprar = real / 7.43

print('Você possuí R$ {:.2f}'.format(real))
print('Você pode comprar US$ {:.2f} dolares.'.format(dolarComprar))
print('Você pode comprar € {:.2f} euros.'.format(euroComprar))
print('Você pode comprar £ {:.2f} libras esterlinas.'.format(libraComprar))
