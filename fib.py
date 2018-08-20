"""Allows the user to find a number in the Fibonacci sequence"""


def fib(n):
    """Returns the number at the n-th position in the Fibonacci sequence"""
    fib = [0, 1]
    if n > 2:
        for i in range(n):
            fib.append(fib[-1] + fib[-2])
        return fib[n-1]
    else:
        return fib[n-1]
