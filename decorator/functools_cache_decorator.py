# @functools.cache

import functools

# function without cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# self-made cache
def fibonacci_sm_cache(n, cache = {}):
    if n in cache:
        return cache[n]

    if n == 0:
        return 0
    if n == 1:
        return 1

    cache[n] = fibonacci(n-1, cache) + fibonacci(n-2, cache)
    return cache[n]

# functools cache
@functools.cache
def fibonacci_ft_cache(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(40))