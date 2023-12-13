"""
Demonstrates a function
which takes an argument
and returns a value
"""


def times_two(n):
    return n * 2


for i in range(1, 11):
    result = times_two(i)
    print(i, result)
