memo = {}


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return memo[n]


print(fibonacci(10))
