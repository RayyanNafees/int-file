import sys
import math
sys.set_int_max_str_digits(10000)
# import basify
BYTE_CONST = 2.408116385911179


def file_to_int(path: str) -> int:
    '''Converts bytes inside a file to integers

    Args:
        path (str): Path to the file

    Returns:
        int: The bytes of the file as integers
    '''
    with open(path, 'rb') as file:
        bins = file.read()

    return int.from_bytes(bins, byteorder='big')


def int_to_file(num: int, path: str) -> None:
    '''Makes the file from integeral value of its bytes

    Args:
        n (int): Integer Value
        path (str): Path to the file
    '''
    intlen = len(str(num))
    bytelen = math.floor(intlen/BYTE_CONST)

    # print(intlen, f(intlen))

    byts = num.to_bytes(bytelen, byteorder='big')

    with open(path, 'wb') as b:
        b.write(byts)
