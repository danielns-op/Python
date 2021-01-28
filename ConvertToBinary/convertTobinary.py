# convertTobinary ####################################################### #
#                                                                         #
# Author: Daniel Noronha                                                  #
#  Email: danielnoronha.sh@gmail.com                                      #
# GitHub: https://github.com/danielns-op/Python/tree/main/ConvertToBinary #
#                                                                         #
# ####################################################################### #


def convert_binary(value):
    """
    Converts any value entered in the value parameter to binary,
    if it is INT or FLOAT it will be converted to STRING.
    :param value: Receive the amount that will be converted to
    STRING and transformed into binary.
    :return: Returns the value in binary.
    """
    binary = ''.join(format(char, 'b') for char in bytearray(str(value), 'utf-8'))
    return binary
