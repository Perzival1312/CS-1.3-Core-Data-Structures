#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace

num_string_upper = string.digits + string.ascii_uppercase
num_string_lower = string.digits + string.ascii_lowercase

def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    result = 0
    # dig_arr = []
    current_num_string_upper = num_string_upper[0:base]
    current_num_string_lower = num_string_lower[0:base]

    # turn number into a reversed array
    digits = list(digits[::-1])
    # for digit in str(digits):
    #     dig_arr.append(digit)
    # reverse the array so that the index is the power of the base
    # dig_arr = dig_arr[::-1]
    # create the base 10 number
    for ind, digit in enumerate(digits):
        # print(ind, digit)
        if current_num_string_upper.__contains__(digit):
            result += int(current_num_string_upper.index(digit)) * (base**ind)
        elif current_num_string_lower.__contains__(digit):
            result += int(current_num_string_lower.index(digit)) * (base**ind)
        else:
            raise ValueError('{} is not a valid number in base {}'.format(digits, base))
    return result

# TODO: Can these functions be re-written using binary as the "go-between"
#       So decode returns binary and encode takes in binary
# def decode2(digits, base):
#     assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

#     base = 2

#     result = 0
#     dig_arr = []
#     current_num_string_upper = num_string_upper[0:base]
#     current_num_string_lower = num_string_lower[0:base]



#     return (result, dig_arr, current_num_string_lower, current_num_string_upper)


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    number = int(number)
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    number += 1
    length = 0
    current_digit_set = num_string_lower[0:base]
    # gets the length of the number in the new base
    for i in range(number):
        if base**i < number:
            length += 1
        else:
            break
    # Creates an array for the new number
    new_num = ['0' for _ in range(length)]

    # for each digit in new num to find that digit
    for ind in range(len(new_num)):
        # checkand find larget possible digit that works
        for possibility in reversed(current_digit_set):
            # get possible number
            num = int(current_digit_set.index(possibility)) * (base**(len(new_num)-1-ind))
            # if possible number is less than input number
            # meaning that the specified digit can work in 
            # specified position.
            if num < number:
                new_num[ind] = possibility
                # decrement input number by added number
                # in newly created number
                number -= num
                # stop checking possibilities
                break
    
    result = ''.join(new_num)
    return result




def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)

    return encode(decode(digits, base1), base2)


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))

    elif len(args) == 2:
        # print(encode(int(args[0]), int(args[1])))
        print(decode(args[0], int(args[1])))
    
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
