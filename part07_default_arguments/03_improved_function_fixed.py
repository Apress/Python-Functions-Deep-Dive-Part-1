def say_greeting(greeting, name, times=1):
    for _ in range(times):
        print(greeting, name)


def very_friendly():
    say_greeting('Hallo', 'Saskia', 3)


def friendly():
    say_greeting('Hello', 'Sam')
    say_greeting('Bonjour', 'Alex')

friendly()
very_friendly()
