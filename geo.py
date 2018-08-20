"""Allows the user to find the square, cube, and triangle of a number"""


def square(n):
    """Returns the square of a number"""
    return n*n


def triangle(n):
    """Returns the triangle of a number"""
    tri = 0
    for i in range(n):
        tri += (i+1)
    return tri


def cube(n):
    """Returns the cube of a number"""
    return n*n*n
