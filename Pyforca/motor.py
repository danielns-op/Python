import artes
import palavras
from random import choice

vida = 6
mostrar = []


def escolhe_nivel_palavra():
    print('-=' * 30)
    print('''
          Escolha um nível:
          [ 1 ] - Fácil
          [ 2 ] - Normal
          [ 3 ] - Difícil''')
    while True:
        try:
            opcao = int(input('Opção: '))
            if opcao == 1:
                nivel = palavras.palavras_faceis
                break
            elif opcao == 2:
                nivel = palavras.palavras_normal
                break
            elif opcao == 3:
                nivel = palavras.palavras_dificeis
                break
            else:
                print('Atenção! Favor informar escolher opção 1, 2 ou 3.')    
        except ValueError:
            print('[ERRO] - Informe apenas número.')
    escolha = choice(nivel)
    return escolha
           
            
def valida_vogal(supor, palavra_escolhida):
    lista_vogal = []
    if supor == 'a':
        lista_vogal = palavras.vogal_a
    elif supor == 'e':
        lista_vogal = palavras.vogal_e
    elif supor == 'i':
        lista_vogal = palavras.vogal_i
    elif supor == 'o':
        lista_vogal = palavras.vogal_o
    elif supor == 'u':
        lista_vogal = palavras.vogal_u
    
    for index in range(len(palavra_escolhida)):
        for vogal in lista_vogal:
            if vogal == palavra_escolhida[index]:
                mostrar[index] = vogal
            

def execucao(nome, vidas):
    palavra = nome
    letra_supor = ''

    for _ in range(len(palavra)):
        mostrar.append('_')

    while True:
        supor = str(input('Adivinhe uma letra: ')).strip().lower()
        if len(supor) != 1:
            print('Atenção! Informe apenas uma letra.')
        elif supor.isnumeric():
            print('[ERRO] - Informe apenas letra.')
        else:
            if supor in 'aeiou':
                valida_vogal(supor, palavra)
            for index in range(len(palavra)):
                if supor == palavra[index]:
                    mostrar[index] = supor
            if supor not in palavra:
                letra_supor += supor
                vidas -= 1
            if vidas < 0:
                print(f'Você perdeu, a palavra é {palavra}')
                break
            print(f'{" ".join(mostrar)}')
            if "_" not in mostrar:
                print('Parabéns!!! Você venceu!')
                break
        print(artes.estagio[vidas])
        print(f'{"-".join(letra_supor)}')


escolhe_palavra = escolhe_nivel_palavra()
execucao(escolhe_palavra, vida)