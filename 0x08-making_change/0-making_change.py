#!/usr/bin/python3
'''A script that returns the perimeter of the island described in grid.'''


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize dp array
    dp = [total + 1] * (total + 1)
    dp[0] = 0  # Base case: no coins are needed to make 0

    # Build up dp array
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If we found a solution, dp[total] will not be total + 1
    return dp[total] if dp[total] != total + 1 else -1