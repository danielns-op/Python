n = input('Digite algo: ')

print('O tipo primitivo desse valor é {}'.format(type(n)))
print('Só tem espaços? {}'.format(n.isspace()))
print('É um número? {}'.format(n.isnumeric()))
print('É alfabético? {}'.format(n.isalpha()))
print('É Alfanumérico? {}'.format(n.isalnum()))
print('Está em maiúsculas? {}'.format(n.isupper()))
print('Está em minúsculas? {}'.format(n.islower()))
# Solução do Guanabara para se está capitalizada
print('Está capitalizada? ', n.istitle())
# Minha solução para se está capitalizada
# print('Está capitalizada? {}'.format(n == n.capitalize()))
