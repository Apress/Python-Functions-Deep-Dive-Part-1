def say_more(main_text, extra_text=[]):
    extra_text.insert(0, main_text)
    for line in extra_text:
        print(line)
    print('-------')

say_more('A hello', ['Plus a few more lines', 'like this'])

say_more('A simple hello')

say_more('Another simple hello')
