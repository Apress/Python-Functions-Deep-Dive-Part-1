# Old version
# def remove_prefixes(name):
#     return name.lstrip('van ').lstrip('de ')

# print(sorted(dutch_surnames, key=remove_prefixes))

dutch_surnames = [
    'de Jong', 'Jansen', 'de Vries',
    'Bakker', 'van Dijk', 'Janssen',
    'Visser', 'Smit', 'de Boer'
]

print('Plain sorted:')
print(sorted(dutch_surnames), '\n')

print('Correct name order:')

# New version
print(sorted(dutch_surnames, key=lambda name: name.lstrip('van ').lstrip('de ')))
