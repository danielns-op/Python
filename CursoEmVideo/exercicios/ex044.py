pprod = float(input('Preço do produto: '))
cpag = str(input('''Forma de pagamento:
\t1 - á vista: dinheiro/cheque
\t2 - á vista: cartão
\t3 - 2x no cartão
\t4 - 3x ou mais no cartão
opção: '''))
desconto = ''
nvalor = 0

if cpag == '1':
    nvalor = pprod - (pprod * 0.1)  # 10% de desconto
    desconto = '10%'
    print('''
    Preço do produto: R$ {:.2f}
    Opção pagamento: {}
    Desconto: {}
    Valor final: R$ {:.2f}
    '''.format(pprod, cpag, desconto, nvalor))
elif cpag == '2':
    nvalor = pprod - (pprod * 0.05)  # 5% de desconto
    desconto = '5%'
    print('''
    Preço do produto: R$ {:.2f}
    Opção pagamento: {}
    Desconto: {}
    Valor final: R$ {:.2f}
    '''.format(pprod, cpag, desconto, nvalor))
elif cpag == '3':
    nvalor = pprod  # não há desconto
    desconto = '0%'
    print('''
    Preço do produto: R$ {:.2f}
    Opção pagamento: {}
    Desconto: {}
    Valor final: R$ {:.2f}
    '''.format(pprod, cpag, desconto, nvalor))
elif cpag == '4':
    nvalor = pprod + (pprod * 0.2)  # 20% de acrescimo
    desconto = '0%, acrescimento de 20%'
    print('''
    Preço do produto: R$ {:.2f}
    Opção pagamento: {}
    Desconto: {}
    Valor final: R$ {:.2f}
    '''.format(pprod, cpag, desconto, nvalor))
else:
    print('Opção inválida.')
