import math
import sys

def num_len(n: int) -> int:
    '''Returns the number of digits in a number n'''
    return 1 if n < 10 else int(math.log10(n)) + 1 

def calculate_byte_const(max_integer: int) -> float:
    '''Derives the byte conversion constant based on empirical analysis'''
    max_bytes = 0
    total_digits = 0
    
    for i in range(1, max_integer + 1):
        num_digits = num_len(i)
        total_digits += num_digits
        max_bytes = max(max_bytes, num_digits)
    
    average_bytes_per_digit = total_digits / max_integer
    byte_const = max_bytes / average_bytes_per_digit
    return byte_const

# Set the maximum integer value for analysis
max_integer = 10**6

# Set a higher precision for printing floating-point numbers
sys.set_float_info(precision=16)

# Calculate the byte conversion constant
BYTE_CONST = calculate_byte_const(max_integer)
print("BYTE_CONST =", BYTE_CONST)

