BASE_NUMBERS = {
    1: 'kere',
    2: 'firi',
    3: 'saran',
    4: 'nani',
    5: 'souli',
    6: 'senni',
    7: 'solofere',
    8: 'solomasara',
    9: 'solomanani',
    10: 'fou',
}

DOUBLE_DIGIT_PREFIX = 'fou nou'


def translate_number(number):
    parts = []

    if number > 10:
        parts.append(DOUBLE_DIGIT_PREFIX)
        number -= 10

    parts.append(BASE_NUMBERS[number])

    print(' '.join(parts))
