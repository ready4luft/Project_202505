def factorial_ZAloop():
    n = int(input("Enter number: "))
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

cache = {}

def factorial_recursive(n):
    if n == 0:
        return 1
    if n in cache:
        return cache[n]
    result = n * factorial_recursive(n - 1)
    cache[n] = result
    return result

print(factorial_ZAloop())
print(factorial_recursive(4))