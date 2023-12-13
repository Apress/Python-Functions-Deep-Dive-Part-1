def my_sum(a, b, c):
    return a + b + c


for a, b, c in [
    [1, 2, 3],
    [5, 10, 100]
]:
    print(a, b, c, 'sum:', my_sum(a, b, c, ))
