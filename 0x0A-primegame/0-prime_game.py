#!/usr/bin/python3
""" Prime Game Module """

MARIA = 0
BEN = 1


def playRound(num):
    """ determines round winner """
    numbers = list(range(num+1))
    primes = []
    for i in range(2, num + 1):
        if numbers[i] != 0:
            primes.append(numbers[i])
            for o_i in range(i * 2, num + 1, i):
                numbers[o_i] = 0
    return BEN if len(primes) % 2 == 0 else MARIA


# def primes(n):
#     """Return list of prime numbers between 1 and n inclusive
#        Args:
#         n (int): upper boundary of range. lower boundary is always 1
#     """
#     prime = []
#     sieve = [True] * (n + 1)
#     for p in range(2, n + 1):
#         if (sieve[p]):
#             prime.append(p)
#             for i in range(p, n + 1, p):
#                 sieve[i] = False
#     return prime


def isWinner(x, nums):
    """ determines winner """
    if x is None or nums is None:
        return None
    ben_wins = 0
    maria_wins = 0
    for i in range(x):
        winner = playRound(nums[i])
        if winner == BEN:
            # print("Ben Wins")
            ben_wins += 1
        else:
            # print("Maria Wins")
            maria_wins += 1
    if ben_wins > maria_wins:
        return "Ben"
    elif ben_wins < maria_wins:
        return "Maria"
    return None
