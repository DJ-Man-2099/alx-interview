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
        current_prime = numbers[0]
        while current_prime <= max_num:
            index = numbers.index(current_prime)
            if index > -1:
                numbers.pop(index)
            current_prime += current_prime
        turn_player = BEN if turn_player == MARIA else MARIA
    return BEN if turn_player == MARIA else MARIA


def isWinner(x, nums):
    """ determines winner """
    if x is None or nums is None or len(nums) != x:
        return None
    ben_wins = 0
    maria_wins = 0
    for i in range(x):
        winner = playRound(nums[i])
        if winner == BEN:
            ben_wins += 1
        else:
            maria_wins += 1
    if ben_wins > maria_wins:
        return "Ben"
    elif ben_wins < maria_wins:
        return "Maria"
    return None
