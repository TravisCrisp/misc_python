import secrets


def gen_password(length, s):

    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    special = '!@#$%^*-?+'

    num_upper = secrets.choice(range(2, int(length / 4)))
    num_digits = secrets.choice(range(2, int(length / 4)))
    num_special = 0
    if s:
        num_special = secrets.choice(range(2, int(length / 4)))
    num_lower = length - num_upper - num_digits - num_special

    choices = []
    result = ''

    for n in range(num_upper):
        choices.append(secrets.choice(upper))

    for n in range(num_digits):
        choices.append(secrets.choice(digits))

    for n in range(num_special):
        choices.append(secrets.choice(special))

    for n in range(num_lower):
        choices.append(secrets.choice(lower))

    for n in range(length):
        choice = secrets.choice(choices)
        result += choice
        i = choices.index(choice)
        choices.pop(i)

    print('\n{}\n'.format(result))

    while True:
        choice = input('Another Password? Yes (y) No (n): ')
        if choice.lower() == 'y':
            return gen_password(get_length(), special_chars())
        elif choice.lower() == 'n':
            break


def get_length():
    while True:
        choice = input('\nNumber of Characters? ')
        if choice.isdigit():
            if int(choice) > 11:
                return int(choice)
            else:
                print('\nMust be 12 or More Characters!')
        print('\nPlease Enter a Number!')


def special_chars():
    while True:
        choice = input('\nSpecial Characters? Yes (y) No (n): ')
        if choice.lower() == 'y':
            return True
        elif choice.lower() == 'n':
            return False


if __name__ == '__main__':
    gen_password(get_length(), special_chars())
