"""
An example docstring for a complex function, e.g. used to generate documentation
"""
def calculate_median(numbers):
    """
    Calculates the median value of a list of numbers
    odd length, e.g. length = 9, take the 5th element, at index 4
    even, e.g. length = 10, take the 5th and 6th elements, at indices 4 and 5
    """
    half_length = len(numbers) // 2
    if len(numbers) % 2 == 0:
        return (numbers[half_length - 1] + numbers[half_length]) / 2
    else:
        return numbers[half_length]

print('__doc__:', __doc__)
print('calculate_median.__doc__:', calculate_median.__doc__)
print('Results:')
for numbers in [
    [0, 0, 1, 0, 0],
    [0, 0, 1, 2, 0, 0],
    [1, 2, 3, 4, 5, 6]
]:
    print(numbers, calculate_median(numbers))
