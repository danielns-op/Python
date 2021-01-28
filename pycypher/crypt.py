import char


def get_data():
    print('-=' * 30)
    message = str(input('Type your message:\n'))
    print('-=' * 30)
    keyword = str(input('---> Write your keyword: '))

    return message, keyword


def encrypt(msg, key):
    encrypted_text = ''
    cod = len(key)
    set_char = char.characters

    for character in msg:
        position = set_char.index(character)
        if position + cod > (len(set_char) - 1):
            position += cod
            encrypted_text += set_char[position - (len(set_char) - 1)]
        else:
            encrypted_text += set_char[position + cod]

    print(f'Its encoded text is:\n {encrypted_text}')


def decrypt(msg, key):
    decoded_text = ''
    cod = len(key)
    set_char = char.characters

    for character in msg:
        position = set_char.index(character)
        if position - cod < 0:
            position -= cod
            # The negative value must be added to the positive value
            # so that it reduces the position in the list.
            # e.g. -5 + 30 = 25
            decoded_text += set_char[position + (len(set_char) - 1)]
        else:
            decoded_text += set_char[position - cod]
    print(f'Your decoded text is:\n {decoded_text}')
