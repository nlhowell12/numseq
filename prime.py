"""Module for finding and checking prime numbers"""
from itertools import count, islice
from math import sqrt


def is_prime(m):
    """Checks if a given number is prime"""
    if m < 2:
        return False
    for number in islice(count(2), int(sqrt(m) - 1)):
        if m % number == 0:
            return False
    return True


def primes(n):
    """Finds all prime numbers less than n"""
    primes = []
    for num in range(2, n):
        if is_prime(num):
            primes.append(num)
    return primes



