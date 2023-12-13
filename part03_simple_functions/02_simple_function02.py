"""
Demonstrates a function which takes an argument
but which does not return anything
"""


def say_hello_multiple_times(n):
    print(f'Saying hello {n} time(s)')
    for _ in range(n):
        print('Hello')
    print()


say_hello_multiple_times(3)
say_hello_multiple_times(0)
say_hello_multiple_times(1)
