import char
import convertTobinary as cvt


def get_data():
    print('-=' * 30)
    message = str(input('Type your message:\n'))
    print('-=' * 30)
    keyword = str(input('---> Write your keyword: '))

    return message, keyword


def generate_cod(value):
    cod_bin = cvt.convert_binary(value)
    generated_cod = 0
    for num in str(cod_bin):
        if num == '1':
            generated_cod += 0.8
        else:
            generated_cod += 0.1
    return round(int(generated_cod))


def encrypt(msg, key):
    encrypted_text = ''
    cod = generate_cod(key)
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
    cod = generate_cod(key)
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
