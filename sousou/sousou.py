SINGLE_DIGITS = {
    1: 'kere',
    2: 'firi',
    3: 'saran',
    4: 'nani',
    5: 'souli',
    6: 'senni',
    7: 'solofere',
    8: 'solomasara',
    9: 'solomanani',
}


def translate_number(number):
    output = ''
    if number > 10:
        output += 'fou nou '
        number -= 10
    elif number == 10:
        output += 'fou'

    if number in SINGLE_DIGITS:
        output += SINGLE_DIGITS[number]

    print(output)
