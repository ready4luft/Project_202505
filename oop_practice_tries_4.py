from functools import wraps

def optimized_cache(func):
    cache = {}
    @wraps(func)  # Сохраняет метаданные функции
    def wrapper(n):
        if n in cache:  # Сначала проверяем кэш
            return cache[n]
        result = func(n)
        cache[n] = result
        return result
    return wrapper

@optimized_cache
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(4))