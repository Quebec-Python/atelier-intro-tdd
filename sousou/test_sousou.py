from sousou import translate_number

SOUSOU_NUMBERS = {
    1: 'kere',
    2: 'firi',
    3: 'saran'
}


def test_given_single_digit_when_translated_then_prints_sousou_number(capsys):
    for number, translation in SOUSOU_NUMBERS.items():
        translate_number(number)

        out, err = capsys.readouterr()
        assert translation in out
