def print_first_vowel(text):
    for character in text:
        if character in 'aeiou':
            print('First vowel in', text, 'is', character)
            return
    print('No vowel in ', text)


print("Return value of print_first_vowel('Hello'):", print_first_vowel('Hello'), '\n')
print("Return value of print_first_vowel('bcdfgh'):", print_first_vowel('bcdfgh'), '\n')

