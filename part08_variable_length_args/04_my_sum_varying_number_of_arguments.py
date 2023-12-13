def my_sum(*numbers):
    print("Type of the 'numbers' argument:", type(numbers))
    print("Value of the 'numbers' argument", numbers, '\n')
    result = 0
    for number in numbers:
        result += number
    return result

print('(empty)', 'sum: ', my_sum(), '\n', '--------')
print(1, 2, 'sum: ', my_sum(1, 2), '\n', '--------')
print(1, 2, 7, 10, 'sum: ', my_sum(1, 2, 7, 10), '\n', '--------')
