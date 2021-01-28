# pyforca.py #################################################### #
#                                                                 #
# Joguinha da forca para se divertir um pouco.                    #
#                                                                 #
#  Autor: Daniel Noronha                                          #
#  Email: danielnoronha.sh@gmail.com                              #
# GitHub: https://github.com/danielns-op/Python/tree/main/Pyforca #
# --------------------------------------------------------------- #
# Utilização:                                                     #
#   Cópia a pasta Pyforca que se encontra no repositório          #
#   acima e execute o arquivo pyforca.py.                         #
#       Ex: python3 pyforca.py                                    #
#                                                                 #
# Caso queira adicionar mais palavras, adicione na lista do       #
# arquivo palavras.py de acordo com a quantidade de letras.       #
#                                                                 #
# v1.3                                                            #
# ############################################################### #
import artes
import motor


def main():
    print(artes.logo)

    vida = motor.vida
    palavra_escolhida = motor.escolhe_nivel_palavra()
    motor.execucao(palavra_escolhida, vida)


if __name__ == '__main__':
    main()
