""" from numba import njit

@njit
def fib_numba(n):
    if n <= 1: return n
    else: return fib_numba(n-1) + fib_numba(n-2)
    


print(fib_numba(47)) """

import platform
print(platform.architecture())