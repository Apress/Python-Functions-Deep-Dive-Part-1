def say_greetings(greeting, name, times):
    for _ in range(times):
        print(greeting, name)
    print()


say_greetings(greeting='Hello', name='Sam', times=4)
say_greetings(greeting='Bonjour', name='Alex', times=5)
