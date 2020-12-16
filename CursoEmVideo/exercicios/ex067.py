while True:
    numero = int(input('Tabuada de qual valor [-1 para sair]: '))
    print(f'Tabuada do número {numero}')
    if numero < 0:
        break
    else:
        for digito in range(1, 11):
            resultado = numero * digito
            print(f'{numero} x {digito:>2} = {resultado:>2}')
print("Saindo.")
