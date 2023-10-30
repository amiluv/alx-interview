#!/usr/bin/python3
<<<<<<< HEAD
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
=======
'''A module for working with Pascal's triangle.
'''


def pascal_triangle(n):
    '''Creates a list of lists of integers representing
    the Pascal's triangle of a given integer.
    '''
    triangle = []
    if type(n) is not int or n <= 0:
        return triangle
    for i in range(n):
        line = []
        for j in range(i + 1):
            if j == 0 or j == i:
                line.append(1)
            elif i > 0 and j > 0:
                line.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(line)
    return triangle
>>>>>>> 0344cabfdafc2ff93868edc51db54f910adf4477
