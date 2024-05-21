#!/usr/bin/python3
""" Task 1 """


from functools import reduce
import math
from typing import List


def len_1(c: int) -> bool:
    """checks first case"""
    return c >> 7 == 0b0


def other_chars(c: int) -> bool:
    """checks other cases"""
    return c >> 6 == 0b10


len_2 = [
    lambda c: c >> 5 == 0b110,
    *([other_chars]*1)
]

len_3 = [
    lambda c: c >> 4 == 0b1110,
    *([other_chars]*2)
]

len_4 = [
    lambda c: c >> 3 == 0b1_1110,
    *([other_chars]*3)
]


def check_utf(chars: List) -> bool:
    """checks each char separately"""
    chars_functions = []
    size = len(chars)
    if size == 1:
        return len_1(chars[0])
    if size == 2:
        chars_functions = list(zip(chars, len_2))
    if size == 3:
        chars_functions = list(zip(chars, len_3))
    if size == 4:
        chars_functions = list(zip(chars, len_4))
    answers = list(map(lambda c: c[1](c[0]), chars_functions))
    return reduce(lambda x, y: x and y, answers)


def validUTF8(data: List[int]) -> bool:
    """determines if a given data set represents a valid UTF-8 encoding"""
    if not data:
        return True

    data = list(map(lambda c: c & 0b1111_1111, data))

    while data:
        size = len(data)
        max_bytes = min(size, 4)
        is_valid = False
        for i in range(max_bytes, 0, -1):
            temp = data[0:i]
            result = check_utf(temp)
            if result:
                data = data[max_bytes:]
                is_valid = True
                break
        if not is_valid:
            return False

    return True
