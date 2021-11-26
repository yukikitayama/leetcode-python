"""
__getitem__() is a magic method in Python

"""

import functools

word = 'world'
functools.reduce(dict.__getitem__, word)

