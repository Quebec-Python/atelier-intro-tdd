from sousou import translate_number

SOUSOU_NUMBERS = {
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


def test_given_single_digit_when_translated_then_prints_sousou_number(capsys):
    for number, translation in SOUSOU_NUMBERS.items():
        translate_number(number)

        out, err = capsys.readouterr()
        assert translation in out


def test_given_number_10_when_translated_then_prints_fou(capsys):
    translate_number(10)

    out, err = capsys.readouterr()
    assert 'fou' in out


def test_given_number_11_when_translated_then_prints_fou_nou_kere(capsys):
    translate_number(11)

    out, err = capsys.readouterr()
    assert 'fou nou kere' in out
