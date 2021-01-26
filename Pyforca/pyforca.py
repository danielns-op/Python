import artes
import motor


def main():
    print(artes.logo)

    vida = motor.vida
    palavra_escolhida = motor.escolhe_nivel_palavra()
    motor.execucao(palavra_escolhida, vida)


if __name__ == '__main__':
    main()
