import time

def how_slow(function, n):
    start_time = time.time_ns()
    fibonacci_number = function(n)
    duration = time.time_ns() - start_time
    print(f'{function.__name__}, '
          f'calculating fibonacci({n}): {duration} nano-seconds, '
          f'result {fibonacci_number}')

def fibonacci_recursive(n):
    if n <= 2:
        return 1

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_non_recursive(n):
    if n <= 2:
        return 1

    first = 1
    second = 1
    for _ in range(n - 2):
        first, second = second, first + second
    return second

for n in range(5, 36, 5):
    how_slow(fibonacci_recursive, n)
    how_slow(fibonacci_non_recursive, n)
    print()
