def calc(my_text):
    my_text = my_text.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ').split()
    print(my_text)
    if my_text[1] == '+':
        return (int(my_text[0]) + int(my_text[2]))
    elif my_text[1] == '-':
        return (int(my_text[0]) - int(my_text[2]))
    elif my_text[1] == '*':
        return (int(my_text[0]) * int(my_text[2]))
    else:
        return (int(my_text[0]) / int(my_text[2]))