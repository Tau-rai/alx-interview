#!/usr/bin/python3
"""Minimum number of coins to make change for a given amount"""


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given total"""
    if total <= 0:
        return 0

    # Initialize an array with 'infinity' and set its first element to 0
    coin_list = [float('inf')] * (total + 1)
    coin_list[0] = 0

    # Fill the array
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                coin_list[i] = min(coin_list[i], coin_list[i - coin] + 1)

    # If coin_list[total] is still float('inf'),
    # it means it's not possible to make that total
    return coin_list[total] if coin_list[total] != float('inf') else - 1
