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
    prime = True
    while n % 2 == 0:
        if prime:
            prime = False
        sum += 2
        n /= 2
    while n > 1:
        n_not_changed = True
        for i in range(int(sqrt(n))+1, 1, -1):
            print(i)
            if n % i == 0:
                if prime:
                    prime = False
                if n_not_changed:
                    n_not_changed = False
                n /= i
                sum += i
                break
        if n_not_changed:
            sum += n
            break
    if prime:
        return int(n)
    return int(sum)
