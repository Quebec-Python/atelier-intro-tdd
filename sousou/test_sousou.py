from sousou import translate_number


def test_given_number_one_when_translated_then_prints_kere(capsys):
    translate_number(1)

    out, err = capsys.readouterr()
    assert "kere" in out


def test_given_number_two_when_translated_then_prints_firi(capsys):
    translate_number(2)

    out, err = capsys.readouterr()
    assert "firi" in out


def test_given_number_three_when_translated_then_prints_saran(capsys):
    translate_number(3)

    out, err = capsys.readouterr()
    assert "saran" in out
