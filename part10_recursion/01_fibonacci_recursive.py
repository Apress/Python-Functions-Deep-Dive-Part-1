def fibonacci(n):
    if n <= 2:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

for n in range(1, 20):
    print(n, fibonacci(n))
