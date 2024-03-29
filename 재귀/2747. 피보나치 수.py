n = int(input())
def fibonacci(n):
    cache = [0] * (n + 1)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        cache[0] = 0
        cache[1] = 1
        for i in range(2, n + 1):
            cache[i] = cache[i-1] + cache[i-2]
        return cache[n]

print(fibonacci(n))