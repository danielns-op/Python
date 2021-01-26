import artes
import palavras
from random import choice

vida = 6
mostrar = []
erro = ''


def escolhe_nivel_palavra():
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
           
            
def valida_vogal(supor):
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

    return lista_vogal


def execucao(nome, vidas=vida, letra_supor=erro):
    palavra = nome

    for _ in range(len(palavra)):
        mostrar.append('_')

    while True:
        # váriavel para validar se existe não existe vogais com acentos.
        existe = 0
        
        print(artes.estagio[vidas])
        print(f'Palavra: {" ".join(mostrar)}')
        print(f'Letras erradas: {"-".join(letra_supor)}')
        print('-=' * 30)

        if "_" not in mostrar:
            print('Parabéns!!! Você venceu!')
            break

        supor = str(input('Adivinhe uma letra: ')).strip().lower()

        if len(supor) != 1:
            print('Atenção! Informe apenas uma letra.')
        elif supor.isnumeric():
            print('[ERRO] - Informe apenas letra.')
        else:
            # verifica se existe a vogal com acentos
            if supor in 'aeiou':
                grupo_vogal = valida_vogal(supor)
                for posicao in range(len(palavra)):
                    for vogal in grupo_vogal:
                        # verifica se cada vogal do grupo está na palavra,
                        # Ex: vogal 'e' grupo: ['e', 'é', 'è', 'ê']
                        if vogal == palavra[posicao]:
                            # caso exista uma vogal acentuada, a mesma será mostrada.
                            mostrar[posicao] = vogal
                            existe += 1
                # caso nenhuma volgal do grupo exista é necessário reduzir a vida
                # e mostrar a vogal errada.
                if existe == 0:
                    letra_supor += supor
                    vidas -= 1
            else:
                for posicao in range(len(palavra)):
                    if supor == palavra[posicao]:
                        mostrar[posicao] = supor
                if supor not in palavra:
                    letra_supor += supor
                    vidas -= 1
                if vidas < 0:
                    print(f'Você perdeu, a palavra é {palavra}')
                    break
