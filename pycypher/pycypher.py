import crypt
from time import sleep


def execution():
    while True:
        print('-=' * 30)
        print('Choose an option:')
        print('\t\t[ 1 ] - Encode\n\t\t[ 2 ] - Decode\n\t\t[ q ] - Exit')
        opcao = str(input('Your option: ')).strip().lower()
        print('-=' * 30)

        if opcao == '1':
            mesg, keyw = crypt.get_data()
            crypt.encrypt(msg=mesg, key=keyw)
        elif opcao == '2':
            mesg, keyw = crypt.get_data()
            crypt.decrypt(mesg, keyw)
        elif opcao == 'q':
            print('Exiting the program.')
            sleep(2)
            break
        else:
            print('Invalid option')
            sleep(2)
            continue

        print('Tudo certo!')


execution()
