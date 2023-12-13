def my_sum(a, b, c):
    return a + b + c


for a, b, c, d in [
    [1, 2, 3, 4],
    [5, 10, 100, 1000]
]:
    print(a, b, c, d, 'sum:', my_sum(a, b, c, d))
