def fancy_division(a, b):
    quotient = a // b
    remainder = a % b

    return quotient, remainder


q, r = fancy_division(25, 3)
print('Quotient of 25 / 3 =', q)
print('Remainder of 25 / 3 =', r)
