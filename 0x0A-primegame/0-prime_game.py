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
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False
    return [p for p in range(n + 1) if is_prime[p]]


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
    if not nums or x < 1 or x > 10000 or any(n < 1 or n > 10000 for n in nums):
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    Maria_wins = 0
    Ben_wins = 0

    for n in nums:
        winner = determine_winner(n, primes)
        if winner == "Maria":
            Maria_wins += 1
        else:
            Ben_wins += 1

    if Maria_wins > Ben_wins:
        return "Maria"
    elif Ben_wins > Maria_wins:
        return "Ben"
    else:
        return None
