# Previous version, included for comparison
# def say_greeting(greeting, name):
#     print(greeting, name)


def say_greeting(greeting, name, times):
    for _ in range(times):
        print(greeting, name)


def very_friendly():
    say_greeting('Hallo', 'Saskia', 3)


def friendly():
    say_greeting('Hello', 'Sam')
    say_greeting('Bonjour', 'Alex')

friendly()
very_friendly()
