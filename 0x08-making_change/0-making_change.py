#!/usr/bin/python3
""" Make Change """


def makeChange(coins, total):
    """ Make change """
    if total <= 0:
        return 0
    
    coins.sort(reverse=True)
    count = 0

    for i in coins:
        while total >= i:
            if total == 0:
                break
            total -= i
            count += 1

    if total == 0:
        return count

    return -1
