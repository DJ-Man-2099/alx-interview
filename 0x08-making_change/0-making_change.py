#!/usr/bin/python3
""" Making Changes Module """


def makeChange(coins, total):
    """ a pile of coins of different values,
    determine the fewest number of coins needed
    to meet a given amount total """

    if total <= 0:
        return 0

    sortedCoins = list(reversed(sorted(coins)))

    count = 0

    for coin in sortedCoins:
        while total > 0 and total >= coin:
            total -= coin
            count += 1

    if total != 0:
        return -1

    return count
