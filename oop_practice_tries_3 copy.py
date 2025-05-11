from functools import lru_cache
import time

def simple_cache(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper

@simple_cache
def factorial_custom(n):
    if n == 0:
        return 1
    return n * factorial_custom(n - 1)

# Замер времени
start = time.time()
factorial_custom(100)
print("Simple_cache:", time.time() - start)    # Пример: 0.0005 сек