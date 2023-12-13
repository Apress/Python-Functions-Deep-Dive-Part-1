def my_sum(**keyword_arguments):
    print('Keyword arguments:')
    for name, value in keyword_arguments.items():
        print(name, '=', value)

    total = 0
    for value in keyword_arguments.values():
        total += value
    return total

print(1, 2, 3, 'sum:', my_sum(a=1, b=2, c=3), '\n')
print(1, 2, 3, 15, 'sum:', my_sum(x=1, y=2, z=3, zz=15))
