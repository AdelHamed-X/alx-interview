def makeChange(coins, total):
    if total <= 0:
        return 0
    
    coins = coins.sort(reverse=True)
    count = 0

    for i in coins:
        if total > i and total > 0:
            total -= i
            count += 1

    if total == 0:
        return count

    return -1
