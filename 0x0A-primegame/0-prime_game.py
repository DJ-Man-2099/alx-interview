#!/usr/bin/python3
""" Prime Game Module """

MARIA = 0
BEN = 1


def playRound(num):
    """ determines round winner """
    turn_player = MARIA
    numbers = list(range(2, num+1))
    while numbers:
        max_num = numbers[-1]
        current_prime = current_number = numbers[0]
        while current_number <= max_num:
            if current_number in numbers:
                numbers.remove(current_number)
            current_number += current_prime
        turn_player = BEN if turn_player == MARIA else MARIA
    return BEN if turn_player == MARIA else MARIA


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
    if x is None or nums is None or x == 0 or nums == []:
        return None
    ben_wins = 0
    maria_wins = 0
    for i in range(x):
        # number_of_primes = len(primes(nums[i]))
        winner = playRound(nums[i])
        if winner == BEN:
            # print(number_of_primes % 2 == 0)
            ben_wins += 1
        else:
            # print(number_of_primes % 2 != 0)
            maria_wins += 1
    if ben_wins > maria_wins:
        return "Ben"
    elif ben_wins < maria_wins:
        return "Maria"
    return None
