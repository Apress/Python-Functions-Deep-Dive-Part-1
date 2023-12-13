def parse_person_entry(entry):
    return entry.split(',')

person = parse_person_entry('Sam,25')
print(person)
