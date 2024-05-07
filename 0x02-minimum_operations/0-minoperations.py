#!/usr/bin/python3
"""
Minimum Operations Task
"""
from math import sqrt


def minOperations(n: int) -> int:
    """Returns the minimum operations to reach n characters in a text file"""
    if n < 2 or not isinstance(n, int):
        return 0
    elif n == 2:
        return 2
    sum = 0
    while n % 2 == 0:
        sum += 2
        n //= 2
    remainder_is_prime = True
    while n > 1:
        # for i in range(3, int(sqrt(n))+1, 2):
        for i in range(3, n+1, 2):
            if n % i == 0:
                # print(f"n: {n}, i: {i}")
                if remainder_is_prime:
                    remainder_is_prime = False
                sum += i
                n //= i
                break
        # if remainder_is_prime:
        #     sum += n
        #     break
    return sum
