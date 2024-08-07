#!/usr/bin/python3
"""
Module for prime game
"""


def sieve_of_eratosthenes(n):
    """
    Return a list of primes up to n using the Sieve of Eratosthenes
    Args: n: an integer
    Returns: a list of prime numbers
    """
    is_prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, n + 1) if is_prime[p]]


def determine_winner(n, primes):
    """
    Determine the winner of the game with given n and primes list
    Args:
        n: the number of integers
        primes: a list of prime numbers
    Returns: the name of the player that won the game
    """
    active = [True] * (n + 1)
    turn = 0  # Maria's turn
    while any(active[1:]):
        move_made = False
        for prime in primes:
            if prime <= n and active[prime]:
                move_made = True
                for multiple in range(prime, n + 1, prime):
                    active[multiple] = False
                break
        if not move_made:
            return "Ben" if turn == 0 else "Maria"
        turn = 1 - turn
    return "Ben" if turn == 0 else "Maria"


def isWinner(x, nums):
    """
    Determine who won the most rounds of the prime game
    Args:
        x: the number of rounds
        nums: an array of integers
    Returns: the name of the player that won the most rounds
    """
    if not nums or x < 1:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    Maria = Ben = 0
    for n in nums:
        winner = determine_winner(n, primes)
        if winner == "Maria":
            Maria += 1
        else:
            Ben += 1

    if Maria == Ben:
        return None
    return "Maria" if Maria > Ben else "Ben"
