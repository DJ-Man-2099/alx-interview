#!/usr/bin/python3
""" Task 1 """


from functools import reduce
import math
from typing import List


def len_1(c: int) -> bool:
    """checks first case"""
    return c >> 7 == 0b0


def len_2(c: int) -> bool:
    """checks second case"""
    return c >> 5 == 0b110


def len_3(c: int) -> bool:
    """checks third case"""
    return c >> 4 == 0b1110


def len_4(c: int) -> bool:
    return c >> 3 == 0b1_1110


def other_chars(c: int) -> bool:
    """checks other cases"""
    return c >> 6 == 0b10


def convert_to_bytes(data):
    return list(map(lambda c: c & 0b1111_1111, data))


# len_2 = [
#     len_2,
#     *([other_chars]*1)
# ]


# len_3 = [
#     len_3,
#     *([other_chars]*2)
# ]


# len_4 = [
#     len_4,
#     *([other_chars]*3)
# ]


# def check_utf(chars: List) -> bool:
#     """checks each char separately"""
#     chars_functions = []
#     size = len(chars)
#     if size == 1:
#         return len_1(chars[0])
#     if size == 2:
#         chars_functions = list(zip(chars, len_2))
#     if size == 3:
#         chars_functions = list(zip(chars, len_3))
#     if size == 4:
#         chars_functions = list(zip(chars, len_4))
#     answers = list(map(lambda c: c[1](c[0]), chars_functions))
#     return reduce(lambda x, y: x and y, answers)


# def validUTF8(data: List[int]) -> bool:
#     """determines if a given data set represents a valid UTF-8 encoding"""
#     if not data:
#         return True

#     data = convert_to_bytes(data)

#     while data:
#         size = len(data)
#         max_bytes = min(size, 4)
#         is_valid = False
#         for i in range(max_bytes, 0, -1):
#             temp = data[0:i]
#             result = check_utf(temp)
#             if result:
#                 data = data[i:]
#                 is_valid = True
#                 break
#         if not is_valid:
#             return False

#     return True

# Optimized answer
def validUTF8(data: List[int]) -> bool:
    """determines if a given data set represents a valid UTF-8 encoding"""
    if not data:
        return True

    data = convert_to_bytes(data)

    byte_count = 0
    for char in data:
        if len_1(char) and byte_count == 0:
            continue
        else:
            if len_2(char) and byte_count == 0:
                byte_count = 1
            elif len_3(char) and byte_count == 0:
                byte_count = 2
            elif len_4(char) and byte_count == 0:
                byte_count = 3
            elif other_chars(char) and byte_count > 0:
                byte_count -= 1
            else:
                return False
    if byte_count != 0:
        return False
    return True


# More Optimized answer
# Credit to:
# https://github.com/
# 7bernie/alx-interview/blob/master/0x04-utf8_validation/0-validate_utf8.py
# #!/usr/bin/python3
# """
# 0-UTF-8 Validation
# "
# def validUTF8(data):
#     """
#     Data: a list of integers
#     Return: True if data is a valid UTF-8
#     encoding, else return False
#     """
#     byte_count =
#     for i in data:
#         if byte_count == 0:
#             if i >> 5 == 0b110 or i >> 5 == 0b1110:
#                 byte_count = 1
#             elif i >> 4 == 0b1110:
#                 byte_count = 2
#             elif i >> 3 == 0b11110:
#                 byte_count = 3
#             elif i >> 7 == 0b1:
#                 return False
#         else:
#             if i >> 6 != 0b10:
#                 return False
#             byte_count -= 1
#     return byte_count ==
