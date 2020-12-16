expressao = str(input('Digite uma expressão qualquer: ')).split()

conta_esquerda = 0
conta_direita = 0

for char in expressao:
    for c in range(0, len(char)):
        if char[c] == '(':
            conta_esquerda += 1
        if char[c] == ')':
            conta_direita += 1

if conta_esquerda == conta_direita:
    print(f'Expressão está certa!')
else:
    print(f'Sua expressão está errada.')
