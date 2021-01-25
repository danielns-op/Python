import artes
import motor


def main():
    print('-=' * 30)
    print(artes.logo)
    print('-=' * 30)

    vida = motor.vida
    palavra_escolhida = motor.escolhe_nivel_palavra()
    motor.execucao(palavra_escolhida, vida)


if __name__ == '__main__':
    main()
