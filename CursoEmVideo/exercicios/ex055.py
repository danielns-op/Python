maior = 0
menor = 0
lista = []
for c in range(1, 6):
    peso = float(input('Informe o peso da {}ª pessoa: '.format(c)))
# Minha solução
    lista.append(peso)
# Solução do Gustavo Guanabara
#   if c == 1:
#       maior = peso
#       menor = peso
#   else:
#       if peso > maior:
#           maior = peso
#       if peso < menor:
#           menor = peso
print('Maior peso: {}\nMenor peso: {}'.format(max(lista), min(lista)))
