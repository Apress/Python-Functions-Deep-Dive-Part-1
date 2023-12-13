def my_sum(*numbers):
    print("Type of the 'numbers' argument:", type(numbers))
    print("Value of the 'numbers' argument", numbers, '\n')
    result = 0
    for number in numbers:
        result += number
    return result


for a, b, c, d in [
    [1, 2, 3, 4],
    [5, 10, 100, 1000]
]:
    print(a, b, c, d, 'sum:', my_sum(a, b, c, d), '\n', '----------')
