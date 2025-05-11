from functools import lru_cache
import time

# Ваш кэш
cache = {}
def factorial_manual(n):
    if n == 0:
        return 1
    if n in cache:
        return cache[n]
    result = n * factorial_manual(n - 1)
    cache[n] = result
    return result

# С lru_cache
@lru_cache(maxsize=None)
def factorial_lru(n):
    if n == 0:
        return 1
    return n * factorial_lru(n - 1)

# Замер времени
start = time.time()
factorial_manual(100)
print("Manual cache:", time.time() - start)  # Пример: 0.000105 сек

start = time.time()
factorial_lru(100)
print("lru_cache:", time.time() - start)    # Пример: 0.000100 сек