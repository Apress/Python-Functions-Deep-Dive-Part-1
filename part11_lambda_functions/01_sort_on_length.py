dutch_surnames = [
    'de Jong', 'Jansen', 'de Vries',
    'Bakker', 'van Dijk', 'Janssen',
    'Visser', 'Smit', 'de Boer'
]
print('Sorted:')
print(sorted(dutch_surnames), '\n')

print('Sorted on length:')
print(sorted(dutch_surnames, key=len))
