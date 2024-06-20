#!/usr/bin/python3
""" Making Changes Module """


def makeChange(coins, total):
    """ a pile of coins of different values,
    determine the fewest number of coins needed
    to meet a given amount total """

    if total <= 0:
        return 0

    count = 0

    # Simple Answer, Doesn't work for all Cases
    sortedCoins = list(reversed(sorted(coins)))

    for coin in sortedCoins:
        while total > 0 and total >= coin:
            total -= coin
            count += 1

    if total != 0:
        return -1

    return count
