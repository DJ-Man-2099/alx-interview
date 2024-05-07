#!/usr/bin/python3
"""
Minimum Operations Task
"""
from math import sqrt


def minOperations(n: int) -> int:
    """Returns the minimum operations to reach n characters in a text file"""
    first_prime = 0
    second_prime = 0
    not_prime = True
    if n < 2:
        return 0
    elif n == 2:
        return 2
    for i in range(int(sqrt(n))+1, 1, -1):
        if n % i == 0:
            not_prime = False
            first_prime = i
            second_prime = n / i
            break
    if not_prime:
        return n
    return int(first_prime + second_prime)
