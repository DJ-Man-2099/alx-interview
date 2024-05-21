#!/usr/bin/python3
""" Task 1 """


# from functools import reduce
# import math
from typing import List


def len_1(c: int) -> bool: return c >> 7 == 0


# def other_chars(c: int) -> bool: return c >> 6 == 2


# len_2 = [
#     lambda c: c >> 5 == 6,
#     *([other_chars]*1)
# ]

# len_3 = [
#     lambda c: c >> 4 == 14,
#     *([other_chars]*2)
# ]

# len_4 = [
#     lambda c: c >> 3 == 30,
#     *([other_chars]*3)
# ]


# def check_utf(chars: List) -> bool:
#     """checks each char separately"""
#     chars_functions = []
#     match len(chars):
#         case 1:
#             return len_1(chars[0])
#         case 2:
#             chars_functions = list(zip(chars, len_2))
#         case 3:
#             chars_functions = list(zip(chars, len_3))
#         case 4:
#             chars_functions = list(zip(chars, len_4))
#     answers = list(map(lambda c: c[1](c[0]), chars_functions))
#     # temp = list(chars_functions)
#     # print("char\t\tfunction used\t\tresult")
#     # for i in range(len(chars)):
#     #     print(
#     #         f"{temp[i][0]}\t\t{temp[i][1]}\t\t{answers[i]}")
#     return reduce(lambda x, y: x and y, answers)


# def try_to_validate(data: List[int], bytes_in_char: int) -> bool:
#     """tries to validate each case"""
#     number_of_chars = int(math.ceil(len(data)/bytes_in_char))
#     # check other chars
#     # check last char
#     # print(f"case number of bytes: {bytes_in_char}")
#     chars = []
#     # data = list(reversed(data))
#     for i in range(number_of_chars):
#         chars.append(data[i*bytes_in_char:(i+1)*bytes_in_char])
#     for char in chars:
#         result = check_utf(char)
#         if result is False:
#             return False

#     return True


# def validUTF8(data: List[int]) -> bool:
#     """determines if a given data set represents a valid UTF-8 encoding"""
#     for i in range(4, 0, -1):
#         if try_to_validate(data, i):
#             return True

#     return False

def validUTF8(data: List[int]) -> bool:
    """tries to validate each case"""
    for char in data:
        # result = len_1(char)
        if char >= 256:
            return False

    return True
