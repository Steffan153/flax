# funcs: holds the functions used by atoms
import functools
import itertools
import math
import more_itertools
import operator
import random

from flax.common import mp, mpc, mpf


def depth(x):
    # depth: returns the depth of x
    return 0 if type(x) != list else (1 if not x else max([depth(a) for a in x]) + 1)


def diagonals(x, anti=False):
    # diagonals: returns the diagonals or the anti-diagonals of x
    diag = [[] for _ in range(len(x) + len(x[0]) - 1)]
    anti = [[] for _ in range(len(diag))]
    min_d = -len(x) + 1

    for i in range(len(x[0])):
        for j in range(len(x)):
            diag[i + j].append(x[j][i])
            anti[i - j - min_d].append(x[j][i])


def divisors(x):
    # divisors: returns the factors of x
    return [a for a in range(1, int(x) + 1) if x % a == 0]


@functools.cache
def fibonacci(x):
    # fibonacci: return the x'th fibonacci number
    if x < 2:
        return x
    else:
        return fibonacci(x - 1) + fibonacci(x - 2)


def find(w, x):
    # find: find the occurence of x in w
    try:
        return iterable(w, digits=True).index(x)
    except ValueError:
        return -1


def flatten(x):
    # flatten: flatten x
    return list(more_itertools.collapse(x))


def iterable(x, digits=False, range_=False):
    # iterable: make sure x is a list
    if type(x) != list:
        if range_:
            return list(range(int(x)))
        elif digits:
            return to_digits(x)
        else:
            return [x]
    else:
        return x


def to_digits(x):
    # to_digits: turn x into a list of digits
    ...
