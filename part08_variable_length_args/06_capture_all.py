def show_arguments(*args, **kwargs):
    if args:
        print('Positional arguments:')
    else:
        print('(no positional arguments)')
    for i, positional_argument in enumerate(args, 1):
        print(i, positional_argument)

    if kwargs:
        print('Keyword arguments:')
        for name, value in kwargs.items():
            print(name, ',', value)
    else:
        print('(no keyword arguments)')

    print('-' * 20)

show_arguments()
show_arguments('a', 'b', 'hello', 10)
show_arguments(name='Alex', times=5)
show_arguments('a', 'b', 'hello', 10, name='Alex', times=5)
