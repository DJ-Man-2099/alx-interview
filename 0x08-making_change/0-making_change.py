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
    # sortedCoins = list(reversed(sorted(coins)))

    # for coin in sortedCoins:
    #     while total > 0 and total >= coin:
    #         total -= coin
    #         count += 1
    ###########################################################################

    min_for_all_coins = [0] + ([float('inf')] * total)

    for i in range(1, total + 1):
        # if i == total:
        #     print(f"current coin: {i}")
        for coin in coins:
            if i < coin:
                break
            # if i == total:
            #     print(f"test coin: {coin}")
            current = i
            count = 0
            while current > 0:
                current -= coin
                count += 1
                if current != 0 and min_for_all_coins[current] < float('inf'):
                    count += min_for_all_coins[current]
                    current = 0
                    # if i == total:
                    #     print(f"new coin found, current min: {count}")
                    break
                # if i == total:
                #     print(f"new coin not found, current min: {count}")
            previous_min = min_for_all_coins[i]
            min_for_all_coins[i] = (count
                                    if current == 0 and count < previous_min
                                    else previous_min)
            # if i == total:
            #     print(f"optimal min: {min_for_all_coins[i]}")
        # print(f"##################################################")

    if min_for_all_coins[total] == float('inf'):
        return -1

    return min_for_all_coins[total]
