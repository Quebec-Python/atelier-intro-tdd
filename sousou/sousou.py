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
    if number in SINGLE_DIGITS:
        translation = SINGLE_DIGITS[number]
        print(translation)
    else:
        print("fou")
