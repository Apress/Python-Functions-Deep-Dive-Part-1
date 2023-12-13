def say_greetings(greeting, name, times):
    for _ in range(times):
        print(greeting, name)
    print()


say_greetings(times=4, greeting='Hello', name='Sam')
say_greetings(greeting='Bonjour', times=5, name='Alex')
