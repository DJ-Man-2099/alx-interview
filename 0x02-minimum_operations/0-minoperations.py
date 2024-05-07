#!/usr/bin/python3
"""
Minimum Operations Task
"""
from math import sqrt


def minOperations(n: any) -> int:
    """Returns the minimum operations to reach n characters in a text file"""
    if n < 2 or not isinstance(n, int):
        return 0
    elif n == 2:
        return 2
    sum = 0
    while n % 2 == 0:
        sum += 2
        n //= 2
    while n > 1:
        for i in range(3, n+1, 2):
            if n % i == 0:
                sum += i
                n //= i
    return int(sum)
