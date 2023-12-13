def show_sum_of_powers(power, *numbers):
    """
    Input: 1, 1, 2, 3, 10

    Output printed:
    1^2 + 2^2 + 3^2 + 10^2 =
    1 + 4 + 9 + 100 =
    114
    """
    total = 0
    numbers_to_be_powered = []
    numbers_powered_as_string = []

    for number in numbers:
        number_powered = number ** power
        numbers_to_be_powered.append(f'{number}^{power}')
        numbers_powered_as_string.append(str(number_powered))
        total += number_powered

    print(' + '.join(numbers_to_be_powered), '=')
    print(' + '.join(numbers_powered_as_string), '=')
    print(total, '\n')

show_sum_of_powers(2, 1, 2, 3, 10)
show_sum_of_powers(3, 1, 2, 3, 10)
