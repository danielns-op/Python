print('-=' * 10)
print('{:^20}'.format('Caixa'))
print('=-' * 10)

conta_produto = maior_que_mil = produto_mais_barato = mais_caro_valor = valor_total = 0
nome_produto_mais_barato = ''

while True:
    nome_produto = str(input('Nome do produto: '))
    preco_produto = float(input('Preço do produto: '))
    conta_produto += 1
    valor_total += preco_produto
    if preco_produto > 1000:
        maior_que_mil += 1
    if conta_produto == 1:
        nome_produto_mais_barato = nome_produto
        produto_mais_barato = preco_produto
    else:
        if preco_produto < produto_mais_barato:
            nome_produto_mais_barato = nome_produto
            produto_mais_barato = preco_produto
    pergunta = str(input('Deseja adicionar mais produtos [S/N]: '))
    while pergunta not in 'SsNn':
        pergunta = str(input('Deseja adicionar mais produtos [S/N]: '))
    if pergunta in 'Nn':
        break

print('-=' * 10)
print(f'''Total da compra foi: R$ {valor_total:.2f}
Total de produtos adicionado: {conta_produto}
{maior_que_mil} produto(s) com valor superior á R$ 1000,00
{nome_produto_mais_barato} foi o produto mas barato com um preço de R$ {produto_mais_barato:.2f}.''')
