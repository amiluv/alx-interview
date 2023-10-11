#!/usr/bin/python3
"""
Create a function def pascal_triangle(n): that returns a list of lists
<<<<<<< HEAD
of integers representing the Pascal’s triangle of n
=======
    of integers representing the Pascal’s triangle of n
>>>>>>> d653ab73826e18d9eda0ea2d90bbc44144fbc001
"""


def pascal_triangle(n):
    res = []
    if n > 0:
        for i in range(1, n + 1):
            level = []
            C = 1
            for j in range(1, i + 1):
                level.append(C)
                C = C * (i - j) // j
            res.append(level)
    return res
<<<<<<< HEAD

=======
>>>>>>> d653ab73826e18d9eda0ea2d90bbc44144fbc001
